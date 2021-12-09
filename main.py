import MaterialSelection as ms
import structurecalc as sc
#import Bucklinganalysis as ba
import numpy as np
import math
import materials as mat

SF = 1.375 #from adsee
P= 1950000 #in Pa, from WP2
m_struct = 852. #Initial strucure mass taken from wp2
m_tank = 90. #Initial tank mass

tank_mat = mat.materials[3]
struct_mat = mat.materials[1]
print(tank_mat["name"])
for i in range(5):
    m_struct, R_struct, t_struct, R_tank_fuel, L_tank_ox = sc.get_dims(m_struct, m_tank, struct_mat)

    t_1_ox, t_2_ox = ms.tank_internal_stresses(P,R_tank_fuel,tank_mat["sigma_yield"],SF)
    t_1_fuel, t_2_fuel = ms.tank_internal_stresses(P,R_tank_fuel,tank_mat["sigma_yield"],SF)


    m_tank_ox = ms.mass_calculation(R_tank_fuel,t_1_ox,t_2_ox,(L_tank_ox-2*R_tank_fuel),tank_mat["rho"])
    m_tank_fuel = ms.mass_calculation(R_tank_fuel,t_1_fuel,t_2_fuel,(0),tank_mat["rho"])
    m_tank = m_tank_ox + m_tank_fuel
print(m_struct,R_tank_fuel, L_tank_ox)
