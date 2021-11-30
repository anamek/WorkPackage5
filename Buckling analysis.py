import math
from basicparameters import *
from MaterialSelection import *
#----------------------------------------------Function definition for buckling analysis--------------------------------

def euler_column_buckling (E, I, A, L):
    sigma_cr = (math.pi ** 2 * E * I) / (A * L ** 2)
    return sigma_cr

def shell_buckling_k (Lambda, L, R, t1, poisson):
    k = Lambda + (12) / (math.pi ** 4) * (L ** 4) / (R ** 2 * t1 ** 2)  * (1 - poisson ** 2) * 1 / Lambda
    return k

def shell_buckling_Q (p, E, R, t1):
    Q = ((p) / (E)) * ((R) / (t1)) ** 2
    return Q

def shell_buckling (Q, k, E, poisson, t1, L):
    sigma_cr = (1.983 - 0.983 * math.exp(-23.14 * Q)) * k * ((math.pi ** 2 * E) / (12 * (1 - poisson ** 2))) * (t1 / L) ** 2
    return sigma_cr

#----------------------------------------------------------Check for buckling failure-----------------------------------
sigma_cr_e = euler_column_buckling(E, I, A, 1) # length still needs to be linked

shell_buckling_k(0.5, 1, R, t_1, poisson)






applied_stress = 0#yet to connect and determine
result = [] #yet to be filled in

print(result[0], result[1])

for i in result:
    if i > applied_stress:
        print("The applied stress is lower the critical stress, therefore this configuration is SAFE")
    elif i < applied_stress:
        print("The applied stress is higher then the critical stress, therefore this configuration is NOT SAFE")
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------WP2 configuration check------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

