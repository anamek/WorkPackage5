import math

#-----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------Function definition for buckling analysis--------------------------------
def moment_of_inertia (t_1, d):
    I = (math.pi * t_1 * d ** 3) / (8)
    return I
def euler_column_buckling (F_ax, E, L, R, t1):
    A = math.pi * 2 * R *t1 
    I = moment_of_inertia(t1, 2*R)
    sigma_cr_euler = (math.pi ** 2 * E * I) / (A * L ** 2)
    return sigma_cr_euler/(F_ax/A)-1, sigma_cr_euler >= F_ax/A

def shell_buckling(F_ax, L, R, t1, P, E):
    poisson = 0.33
    A = math.pi * 2 * R *t1 
    #k = Lambda + (12 / math.pi ** 4) * (L ** 4 / (R ** 2 * t1 ** 2)) * (1 - poisson ** 2) * (1 / Lambda)
    k = k_opt(L, R, t1)
    print(k)
    Q = (P / E) * ((R / t1) ** 2)
    sigma_cr_shell = (1.983 - 0.983 * math.exp(-23.14 * Q)) * k * ((math.pi ** 2 * E) / (12 * (1 - poisson ** 2))) * (t1 / L) ** 2
    return sigma_cr_shell/(F_ax/A)-1, sigma_cr_shell >= F_ax/A

def k_opt(L, R, t1):
    lambda_opt = round(math.sqrt((12 * L**4 * (1-0.33**2))/(math.pi**4 * R**2 * t1**2)))
    lambda_t = 10
    print(lambda_t + (12 * L**4 * (1-0.33**2))/(math.pi**4 * R**2 * t1**2)/lambda_t)
    return 2 * lambda_opt

#----------------------------Check for buckling failure-----------------------------------------------------------------
'''
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
'''
