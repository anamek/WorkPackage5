import MaterialSelection as ms
import structurecalc as sc
import Bucklinganalysis as ba
import numpy as np
import math
import materials as mat
import matplotlib.pyplot as plt

SF_tank = 1.25*1.2*1.05 #from NASA 
SF_struct = 1.25*1.4
P= 1950000 #in Pa, from WP2
m_struct = 852. #Initial strucure mass taken from wp2
m_tank_ox= 50. #Initial tank mass
m_tank_fuel = 40.
n_iter = 6

xs = []
tank_mat = mat.materials[3]
struct_mat = mat.materials[1]
m_other = m_rest = 33.5 + 930.


#iteration loop
print(tank_mat["name"])
for i in range(n_iter):
    m_tank = m_tank_ox + m_tank_fuel
    m_struct, m_ox, m_fuel, R_struct, t_struct, R_tank_fuel, L_tank_ox, L_struct = sc.get_dims(m_struct + m_tank + m_other, struct_mat, SF_struct)
    m_prop = m_ox + m_fuel
    F_z_ox = 3.1 * 9.81 * (m_tank_ox + m_ox)
    F_z_fuel = 3.1 * 9.81 * (m_tank_fuel + m_fuel)
    
    t_1_ox, t_2_ox = ms.tank_internal_stresses(P,R_tank_fuel,tank_mat["sigma_yield"],SF_tank)
    t_1_fuel, t_2_fuel = ms.tank_internal_stresses(P,R_tank_fuel,tank_mat["sigma_yield"],SF_tank)
    buckle = ba.euler_column_buckling(F_z_ox, tank_mat["E"], L_tank_ox, R_tank_fuel, t_1_ox)[1] and ba.shell_buckling(F_z_ox, L_tank_ox, R_tank_fuel, t_1_ox, P, tank_mat["E"])[1]
    
    #i only check the ox tank but buckling does not occur so im not going to bother with the other one
    while not buckle:
        t_1_ox += 0.0001 
        buckle = ba.euler_column_buckling(F_z_ox, tank_mat["E"], L_tank_ox, R_tank_fuel, t_1_ox)[1] and ba.shell_buckling(F_z, L_tank_ox, R_tank_fuel, t_1_ox, P, tank_mat["E"])[1]
    ms_cb = ba.euler_column_buckling(F_z_ox, tank_mat["E"], L_tank_ox, R_tank_fuel, t_1_ox)[0]
    ms_sb = ba.shell_buckling(F_z_ox, L_tank_ox, R_tank_fuel, t_1_ox, P, tank_mat["E"])[0]
        
        #print(t_1_ox)#, ba.euler_column_buckling(F_z, tank_mat["E"], L_tank_ox, R_tank_fuel, t_1_ox)[0])
        
       
    m_tank_ox = ms.mass_calculation(R_tank_fuel,t_1_ox,t_2_ox,(L_tank_ox-2*R_tank_fuel),tank_mat["rho"])
    m_tank_fuel = ms.mass_calculation(R_tank_fuel,t_1_fuel,t_2_fuel,(0),tank_mat["rho"])
    
    xs.append(m_struct)
    #print(m_tank + m_struct + m_other, R_struct, 6, t_struct)
    
#perform some sanity checks:
ms_struct_buckle = sc.crit_buckling_strength(R_struct, L_struct, t_struct, struct_mat["E"])/sc.sigma_tot(R_struct, L_struct, t_struct, 3 * 9.81, 4.1 * 9.81, m_struct + m_tank + m_other+m_prop)-1
ms_tank_h, ms_tank_l = ms.sanity_check(P, R_tank_fuel, t_1_ox, t_2_ox, tank_mat["sigma_yield"])

#print the results
print("\nStructure dimensions dimensions:")
print("Mass={} kg, Radius={} m, L={} m t={}mm".format(round(m_struct*100)/100,math.ceil(R_struct*100)/100, math.ceil(L_struct*100)/100, math.ceil(t_struct*100000)/100))
print("Fuel tank dimensions:")
print("Mass={} kg, Radius={} m, t={}mm".format(round(m_tank_fuel*100)/100, math.ceil(R_tank_fuel*100)/100, math.ceil(t_1_fuel*100000)/100))
print("Oxidizer tank dimensions:")
print("Mass={} kg, Radius={} m, L={} m, t={}mm".format(round(m_tank_ox*100)/100, math.ceil(R_tank_fuel*100)/100, math.ceil(L_tank_ox*100)/100, math.ceil(t_1_fuel*100000)/100))
print("Safety margins")
print("Column buckling: {}, Shell buckling: {}, Buckling of structure: {}, Tank interal press: {} and {}".format(
    round(100*ms_cb)/100, round(100*ms_sb)/100, round(100*ms_struct_buckle)/100, round(100*ms_tank_h)/100, round(100*ms_tank_l)/100))
print(F_z_ox, F_z_fuel)
fig, ax = plt.subplots()
bruh = ax.plot(range(n_iter), xs, "C0", marker="1")
ax.grid(True)
ax.set_xticks(range(n_iter))
ax.set_xlabel("n iterations")
ax.set_ylabel("Structure mass")

plt.show()
