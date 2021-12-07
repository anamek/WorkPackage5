import math
from MaterialSelection import *
#-------------------------------------------Geometric properties--------------------------------------------------------

#--------------------------------------------------Geometric proeprties functions---------------------------------------
#-----------------------------------These functions apply to cross sections at which t1 is present----------------------
#-----------------------------------Thin walled is assumed to apply here------------------------------------------------
def cross_sectional_area (R, t_1):
    area = (math.pi * R ** 2) - (math.pi * (R - t_1) ** 2)
    return area

def moment_of_inertia (R, t_1): #Structural analysis course AE2135 - I Ixx = Iyy as a circle has infinite symetry lines
    I = (math.pi * t_1 * (2 * R) ** 3) / 8
    return I

I = moment_of_inertia(R, t_1)
A = cross_sectional_area(R, t_1)