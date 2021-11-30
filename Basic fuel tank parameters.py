import math
#-------------------------------------------Geometric properties--------------------------------------------------------
l = 1  #[m]
t1 = 0.5 #[m]
t2 = 1 #[m]
r = 1 #[m]
#--------------------------------------------------Geometric proeprties functions---------------------------------------
#-----------------------------------These functions apply to cross sections at which t1 is present----------------------
#-----------------------------------Thin walled is assumed to apply here------------------------------------------------
def cross_sectional_area (r, t1):
    area = (math.pi * r ** 2) - (math.pi * (r - t1) ** 2)
    return area

def moment_of_inertia (r, t1): #Structural analysis course AE2135 - I Ixx = Iyy as a circle has infinite symetry lines
    I = (math.pi * t1 * (2 * r) ** 3) / 8
    return I

