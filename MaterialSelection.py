import math



def tank_internal_stresses(pressure, radius, yield_strength,safety_factor):
    thickness_cylinder= (pressure*radius)/yield_strength*safety_factor
    thickness_sphere=(pressure*radius)/(2*yield_strength)*safety_factor
    #sigma_h = (pressure * radius) / thickness
    #sigma_l = (pressure * radius) / (2 * thickness)
    return thickness_cylinder,thickness_sphere



def mass_calculation(radius,thickness_cylinder, thickness_sphere, height,density):
    mass_cylinder=thickness_cylinder*radius*2*math.pi*height*density
    mass_spherical=radius**2*thickness_sphere*4*math.pi*density
    mass_total=mass_cylinder+mass_spherical
    return mass_total

def sanity_check(P, R, t_cyl, t_sphere,  sigma_yield):
    sigma_h = (P*R)/t_sphere 
    sigma_l = (P*R)/t_cyl
    ms_h = sigma_h/sigma_yield -1
    ms_l = sigma_l/sigma_yield -1
    return ms_h, ms_l
    
    


