import math
from MaterialSelection import *
#-------------------------------------------Geometric properties--------------------------------------------------------

#--------------------------------------------------Geometric proeprties functions---------------------------------------
#-----------------------------------These functions apply to cross sections at which t1 is present----------------------
#-----------------------------------Thin walled is assumed to apply here------------------------------------------------
#Axial loading

def cross_sectional_areac (R, t_1):
    area = (math.pi * R ** 2) - (math.pi * (R - t_1) ** 2)
    return area

def moment_of_inertiac (R, t_1): #Structural analysis course AE2135 - I Ixx = Iyy as a circle has infinite symetry lines
    I = (math.pi * t_1 * ((2 * R) ** 3)) / 8
    return I

Ic = moment_of_inertiac(R, t_1)
Ac = cross_sectional_areac(R, t_1)

print("Axial I:", Ic)
print("Axial A:", Ac)
print("check:", Ic / Ac)
#Lateral loading
def cross_sectional_areal (h, R, d, t_1, t_2):
    areal = ((h - 2 * R) * d - (h - 2 * R) * (d - 2 * t_1)) + ((math.pi * R ** 2) - (math.pi * (R - t_2) ** 2))
    return areal

def moment_of_inertial (t_1, h, R, t_2, d): #Structural analysis course AE2135 - I
    Il = 2 * ((t_1 * (h - 2 * R)) * R ** 2) + ((math.pi * t_2 * d ** 3) / 8)
    return Il

Il = moment_of_inertial(t_1, h, R,t_2, d)
Al = cross_sectional_areal(h, R, d, t_1,t_2)

print("Lateral I:", Il)
print("Lateral A:", Al)
print("check:",Il / Al)






