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
    return V_fuel * vol_margin, V_ox * vol_margin, m_prop

#get length of tank if pill shaped.
def L_tank(R_tank, V):
    R_act = R_tank
    L = (V-(4./3.)*math.pi*R_act**3)/(math.pi * R_act**2) + 2 * R_act
    return L

#get radius of tank if spherical: 
def R_sphere_tank(V):
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
        diffs = np.abs(sigma_tot(R, L, test_ts, 3 * 9.81, 4.1 * 9.81, M)*1.1 - crit_buckling_strength(R, L, test_ts, E))
        t_center = test_ts[np.argmin(diffs)]
        t_min = t_center - step/1.9
        t_max = t_center + step/1.9
          
            
    return t_center

#Main optimization loop
#these are just some values calculated in WP2 or stuff that is constant

def get_dims(m_tot_dry, mat):
    tank_vol_margin = 1.1
    L_struct = 6.
    Delta_V_req = 2300

    #list of volumes for fuel and ox and total mass of propellants
    #obtained from dry mass, delta v and and the extra tank volume required
    *prop_vols, m_prop = get_prop_vol(m_tot_dry, Delta_V_req,tank_vol_margin)
    
    #here we could add a system that accounts for the change in weight of the tank
    #m_tank = 0.46 * sum(prop_vols)
    
    #Then the size of the tank is obtained from geometry
    #Radii are the same for both, L_tank for fuel is twice the radius, L_tank ox is based on geometry
    R_tank_fuel = R_tank_ox = R_sphere_tank(prop_vols[0])
    L_tank_fuel = 2 * R_tank_fuel
    L_tank_ox = L_tank(R_tank_ox, prop_vols[1])
    
    #print(R_tank_fuel, L_tank_ox)
    #radius of structure is the same as fuel tank + 5cm margin
    R_struct = math.ceil((R_tank_fuel + 0.05)*100)/100
    #Al-2024 used for main structure, same tradeoff as in wp2
    mat = materials.materials[1]
    #Based on buckling t is calculated, again same as in wp2. Mass follows from geometry
    t_struct = t_for_buckling(R_struct, L_struct , mat["E"], m_tot_dry + m_prop)
    m_struct = 2 * math.pi * R_struct * t_struct * L_struct * mat["rho"]
    return(m_struct, m_prop, R_struct, t_struct, R_tank_fuel, L_tank_ox, L_struct) 
    



