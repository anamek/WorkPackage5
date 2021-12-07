import math
import matplotlib as plt
from basicparameters import *
from MaterialSelection import *
#----------------------------------------------Function definition for buckling analysis--------------------------------
L = h + 2 * R
def euler_column_buckling (E, I, A, L):
    sigma_cr = (math.pi ** 2 * E * I) / (A * L ** 2)
    return sigma_cr

def shell_buckling_k (Lambda, L, R, t1, poisson):
    k = Lambda + (12 / math.pi ** 4) * (L ** 4 / (R ** 2 * t1 ** 2))  * (1 - poisson ** 2) * (1 / Lambda)
    return k

def shell_buckling_Q (P, E, R, t1):
    Q = (P / E) * ((R / t1) ** 2)
    return Q

def shell_buckling (Q, k, E, poisson, t1, L):
    sigma_cr = (1.983 - 0.983 * math.exp(-23.14 * Q)) * k * ((math.pi ** 2 * E) / (12 * (1 - poisson ** 2))) * (t1 / L) ** 2
    return sigma_cr

#----------------------------------------------------------Check for buckling failure--axial----------------------
sigma_cr_ea = euler_column_buckling(E, Ic, Ac, L) # [MPa]

kc = shell_buckling_k(0.5, L, R, t_1, poisson)
Qc = shell_buckling_Q(P, E, R, t_1)
sigma_cr_sa = shell_buckling(Qc, kc, E, poisson, t_1, L)  #[MPa]
#----------------------------------------------------------Check for buckling failure--Lateral----------------------
sigma_cr_el = euler_column_buckling(E, Il, Al, L) # [MPa]

k = shell_buckling_k(0.5, L, R, t_1, poisson)
Q = shell_buckling_Q(P, E, R, t_1)
sigma_cr_sl = shell_buckling(Q, k, E, poisson, t_1, L)  #[MPa]

applied_stressc = (3 * 9.81 * mass) / Ac #axial
applied_stressl = (4.1 * 9.81 * mass) / Al #lateral

resultc = [sigma_cr_ea / (1 * 10 ** 9), sigma_cr_sa / (1 * 10 ** 9)]
resultl = [sigma_cr_el / (1 * 10 ** 9), sigma_cr_sl / (1 * 10 ** 9)]
print("Critical stress, column buckling, axial:", resultc[0], "Critical stress, shell buckling ", resultc[1], "[GPA]")
print("Critical stress, column buckling:", resultc[0], "Critical stress, shell buckling", resultc[1], "[GPA]")

for i in resultc:
    if i > applied_stressc / (1 * 10 ** 9):
        print("The applied stress is lower the critical stress, therefore this configuration is SAFE")
    elif i < applied_stressc / (1 * 10 ** 9):
        print("The applied stress is higher then the critical stress, therefore this configuration is NOT SAFE")
for i in resultl:
    if i > applied_stressl / (1 * 10 ** 9):
        print("The applied stress is lower the critical stress, therefore this configuration is SAFE")
    elif i < applied_stressl / (1 * 10 ** 9):
        print("The applied stress is higher then the critical stress, therefore this configuration is NOT SAFE")
#-------------outcome of safety check:
#------------1st = column buckling under compression
#------------2nd = shell buckling under compression
#------------3rd = column buckling under lateral loads
#------------4th = shell buckling under lateral loads
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------Iteration procedure------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

