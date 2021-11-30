import numpy as np

f_1 = [1924.7, 1924.7, 1988.9]  # From page 7 in WP4
f_0 = [500, 7306.3, 500]  # From lug_design.py
f_r = np.add(f_0, f_1)
lug_mass = 0.003574  # kg
magnitude = np.linalg.norm(f_r)

print(round(magnitude, 3))

total_compressive_force = 100000.0
number_of_attachments = 1

ratio = magnitude / total_compressive_force
attachment_mass = ratio * lug_mass
total_mass = attachment_mass * number_of_attachments
