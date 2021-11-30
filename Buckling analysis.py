import math

#----------------------------------------------Constant values and list of properties-----------------------------------

#-----------------------------------------------------------------------------------------------------------------------



#----------------------------------------------Function definition for buckling analysis--------------------------------

def euler_column_buckling (E, I, A, L):
    sigma_cr = (math.pi ** 2 * E * I) / (A * L ** 2)
    return sigma_cr

def shell_buckling_k (Lambda, L, R, t1, poisson):
    k = Lambda + (12) / (math.pi ** 4) * (L ** 4) / (R ** 2 * t1 ** 2)  * (1 - poisson ** 2) * 1 / Lambda
    return k

def shell_buckling_Q ():

def shell_buckling ():

