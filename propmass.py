import numpy as np
import math


def get_prop_vol(dry_mass, Delta_V):
    I_sp = 321
    O_F = 1.65
    
    rho_fuel = 880
    rho_ox = 1220
    
    a = math.exp(Delta_V/(9.81*I_sp))
    m_prop = (dry_mass + tank_mass)/a - dry_mass
    
    m_fuel = m_prop/(1+1.65)
    m_ox = m_prop - m_fuel
    
    V_fuel = m_fuel * rho_fuel
    V_ox = m_ox * rho_ox
    
    return V_fuel, V_ox


#get length of tank if pill shaped.
def L_tank(R_struct, V):
    R_act = R_struct - inside_margin
    L = ((V-(4./3.)*math.pi)*R_act**3)/(math.pi * R_act**2) + 2 * R_act**2 
    return L

#get radius of tank if spherical: 
def R_tank(V):
    R = math.pow((3.*V)/(4.*math.pi()), 1./3.)
    return R


m_struct = 793
m_tank = 90
prop_vols = get_prop_vol(930 + m_struct, 2300)
print(prop_vols)
    




