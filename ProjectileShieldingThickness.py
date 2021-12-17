import math

K = 0.7
m = 10 ** (-10)  # g
rho = 3.4  # g/cm3
GM = 6.8351 * (10 ** 6)  # km3/s2
r = 1750 + 24764  # km
u = 7.7  # km/s

v_esc = math.sqrt((2 * GM) / r)
v_r = math.sqrt(v_esc ** 2 + u ** 2)
v_orbit = math.sqrt(GM / r)

t = K * m ** 0.352 * (v_r + v_orbit) ** 0.875 * rho ** 0.167

print(t)
