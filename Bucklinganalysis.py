import math
import matplotlib as plt
import basicparameters
#----------------------------------------------Function definition for buckling analysis--------------------------------

def euler_column_buckling (E, I, A, L):
    sigma_cr_euler = (math.pi ** 2 * E * I) / (A * L ** 2)
    return sigma_cr_euler

def shell_buckling (Lambda, L, R, t1, poisson, P, E):
    k = Lambda + (12 / math.pi ** 4) * (L ** 4 / (R ** 2 * t1 ** 2)) * (1 - poisson ** 2) * (1 / Lambda)
    Q = (P / E) * ((R / t1) ** 2)
    sigma_cr_shell = (1.983 - 0.983 * math.exp(-23.14 * Q)) * k * ((math.pi ** 2 * E) / (12 * (1 - poisson ** 2))) * (t1 / L) ** 2
    return sigma_cr_shell

#----------------------------------------------------------Check for buckling failure--axial and lateral----------------
def buckling_check (sigma_cr_euler, sigma_cr_shell, applied_stress):
    if sigma_cr_euler > applied_stress:
        print("The critical stress for the euler buckling mode is:", sigma_cr_euler)
        print("The component is SAFE under applied loading")
    elif sigma_cr_euler < applied_stress:
        print("The critical stress for the euler buckling mode is:", sigma_cr_euler)
        print("The component is NOT SAFE under applied loading, iteration is needed")

    if sigma_cr_shell > applied_stress:
        print("The critical stress for the shell buckling mode is:", sigma_cr_shell)
        print("The component is SAFE under applied loading")
    elif sigma_cr_shell < applied_stress:
        print("The critical stress for the euler buckling mode is:", sigma_cr_euler)
        print("The component is NOT SAFE under applied loading, iteration is needed")

#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------Iteration procedure------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

