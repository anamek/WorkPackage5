import numpy as np
import math
import materials

def get_prop_vol(dry_mass, Delta_V, vol_margin):
    I_sp = 321
    O_F = 1.65
    
    rho_fuel = 880
    rho_ox = 1220
    
    a = math.exp(Delta_V/(9.81*I_sp))
    m_prop = (dry_mass*a) - dry_mass
    
    m_fuel = m_prop/(1+1.65)
    m_ox = m_prop - m_fuel
    
    V_fuel = m_fuel / rho_fuel
    V_ox = m_ox / rho_ox
    
    return V_fuel * vol_margin, V_ox * vol_margin


#get length of tank if pill shaped.
def L_tank(R_tank, V):
    R_act = R_tank
    L = (V-(4./3.)*math.pi*R_act**3)/(math.pi * R_act**2) + 2 * R_act
    return L

#get radius of tank if spherical: 
def R_tank(V):
    R = math.pow((3.*V)/(4.*math.pi), 1./3.)
    return R

def crit_buckling_strength(R, L, t, E):
    return (9 * np.power((t/R), 1.6) + 0.16 * np.power((t/L), 1.3)) * E

def sigma_tot(R, L, t, gy, gx, M):
    sigma_bend = (gy * L * M * R)/(math.pi * R**3 * t) * 0.5
    sigma_norm = (gx *M)/(2 * math.pi * R * t)
    return (sigma_bend + sigma_norm) * 1.5625
    
def t_for_buckling(R, L, E, M):
    
    t_min = 0.001
    t_max = 0.1
    samples = 100
    delta = 1
    #while delta > 1e-6:
    for i in range(10):
        
        step = (t_max - t_min)/samples
        
        test_ts = np.linspace(t_min, t_max, samples)
        diffs = np.abs(sigma_tot(R, L, test_ts, 3 * 9.81, 4.1 * 9.81, M) - crit_buckling_strength(R, L, test_ts, E))
        t_center = test_ts[np.argmin(diffs)]
        t_min = t_center - step/1.9
        t_max = t_center + step/1.9
        
            
            
    return t_center

tank_vol_margin = 1.1
m_struct = 885.5
m_tank = 90.
for i in range(10):
    prop_vols = get_prop_vol(930 + m_struct + m_tank, 2300,tank_vol_margin)

    m_tank = 0.46 * sum(prop_vols)
    R_tank_fuel = R_tank_ox = R_tank(prop_vols[0])
    L_tank_fuel = 2 * R_tank_fuel
    L_tank_ox = L_tank(R_tank_ox, prop_vols[1])

    #radius of structure is the same as fuel tank + 5cm margin
    R_struct = math.ceil((R_tank_fuel + 0.05)*100)/100
    L_struct = (L_tank_fuel + L_tank_ox)*1.5
    L_struct = 6
    mat = materials.materials[1]
    t_struct = t_for_buckling(R_struct, L_struct , mat["E"], 3762.)
    m_struct = 2 * math.pi * R_struct * t_struct * L_struct * mat["rho"]
    print(R_struct, L_struct, t_struct, m_struct)




