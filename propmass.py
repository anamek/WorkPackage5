import numpy as np
import math


def get_prop_vol(dry_mass, tank_mass):
    I_sp = 321
    Delta_V = 2300
    O_F = 1.65
    
    rho_fuel = 880
    rho_ox = 1220
    
    a = math.exp(Delta_V/(9.81*I_sp))
    m_prop = (dry_mass + tank_mass)/a - dry_mass - tank_mass
    
    m_fuel = m_prop/(1+1.65)
    m_ox = m_prop - m_fuel
    
    V_fuel = m_fuel * rho_fuel
    V_ox = m_ox * rho_ox
    
    return V_fuel, V_ox



def L_tank(R_struct, V, inside_margin):
    R_act = R_struct - inside_margin
    L = ((V-(4./3.)*math.pi)*R_act**3)/(math.pi * R_act**2) + 2 * R_act**2 
    return L


    




