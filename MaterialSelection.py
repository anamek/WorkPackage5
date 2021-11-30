def tank_internal_stresses(pressure, radius, thickness):
    sigma_h = (pressure * radius) / thickness
    sigma_l = (pressure * radius) / (2 * thickness)