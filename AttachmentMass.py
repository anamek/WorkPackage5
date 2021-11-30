import numpy as np
# WP 4 forces; [500, 7306.3, 500] F_1 = [1924.7, 1924.7, 1988.9]

f_1 = [1924.7, 1924.7, 1988.9]
f_0 = [500, 7306.3, 500]
f_t = np.add(f_0,f_1)
magnitude = np.linalg.norm(f_t)

print(round(magnitude,3))

total_compressive_force =
number_of_attachments = 1
