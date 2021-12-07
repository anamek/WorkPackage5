R= 0.614       #in meters
d = 2 * R
P= 1950000 #in Pa, from WP2
h= 2 * R                         #arbitrary this is a cinfiguration of a sphere
rho= 4520    #aluminium (kg/m3)
SF= 1.375 #from ADSEE
sigma_y= 880000000 #Pa, aluminum 2024 T3
E = 73.1 * 10 ** 9 #Pa, aluminim 2024 T3
poisson = 0.33  #v, aluminium 2024 T3
def tank_internal_stresses(pressure, radius, yield_strength,safety_factor):
    thickness_cylinder= (pressure*radius)/yield_strength*safety_factor
    thickness_sphere=(pressure*radius)/(2*yield_strength)*safety_factor
    #sigma_h = (pressure * radius) / thickness
    #sigma_l = (pressure * radius) / (2 * thickness)
    return thickness_cylinder,thickness_sphere

t_1=tank_internal_stresses(P,R,sigma_y,SF)[0]
t_2=tank_internal_stresses(P,R,sigma_y,SF)[1]
print("Required thickness of the cylinder: ",t_1,"\nRequired thickness of the spherical end caps",t_2)

def mass_calculation(radius,thickness_cylinder, thickness_sphere, height,density):
    mass_cylinder=thickness_cylinder*radius*2*3.14*height*density
    mass_spherical=radius**2*thickness_sphere*4*3.14*density
    mass_total=mass_cylinder+mass_spherical
    return mass_total

mass = mass_calculation(R,t_1,t_2,h,rho)


print("Mass of the tank: ",mass)
