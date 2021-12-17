import numpy as np
import math
import matplotlib.pyplot as plt
import materials as mats
omega_f = 100. /  (2.*math.pi)
#m = 486.59
#k = 396e6/2
m= 788.42
k = 351e6
k = ((0.52*0.00178*2*math.pi)*mats.materials[3]["E"])/1.18
print(k)

omega_n = math.sqrt(k/m)
F = 9.81*3.0 *m
A_p = lambda wf: F/(m*(omega_n**2 - wf**2))
A_p_max = A_p(omega_f)
A_c = -(A_p_max*omega_f)/omega_n

print(omega_f, omega_n, A_p_max, A_c)

    


ts = np.linspace(0,1,3000)
omega_fs = np.linspace(0, omega_f, 1000)
xs = lambda t: A_c * np.sin(omega_n * t) + A_p_max * np.sin(omega_f *t)
fig, ax = plt.subplots()
#fig1, ax1 = plt.subplots()
ax.plot(ts, xs(ts), "C0")
#ax1.plot(omega_fs, A_p(omega_fs), "C1")
plt.show()
#fig.savefig("wp5_forcedvibes.pdf")
#fig1.savefig("wp5_forcedvibes_A_p.pdf")
