import math



def tank_internal_stresses(pressure, radius, yield_strength,safety_factor):
    thickness_cylinder= (pressure*radius)/yield_strength*safety_factor
    thickness_sphere=(pressure*radius)/(2*yield_strength)*safety_factor
    sigma_h = (pressure * radius) / thickness
    sigma_l = (pressure * radius) / (2 * thickness)
    return thickness_cylinder,thickness_sphere, sigma_h, sigma_l



def mass_calculation(radius,thickness_cylinder, thickness_sphere, height,density):
    mass_cylinder=thickness_cylinder*radius*2*math.pi*height*density
    mass_spherical=radius**2*thickness_sphere*4*math.pi*density
    mass_total=mass_cylinder+mass_spherical
    return mass_total




