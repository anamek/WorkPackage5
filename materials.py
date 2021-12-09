import numpy as np
import math

materials = [   
    {"name": "al-7075T6", "E": 71.7*(10**9), "sigma_yield": 503*(10**6), "tau_yield": 331.*(10**6), 
    "sigma_ult": 572.*(10**6), "alpha": 2.385*(10**-5), "rho":2810.,"pois":0.33},
    {"name": "al-2024T3", "E": 73.1*(10**9), "sigma_yield": 345*(10**6), "tau_yield": 283.*(10**6),
    "sigma_ult": 483. *(10**6), "alpha": 2.322*(10*-5), "rho": 2780., "pois":0.33},
    {"name": "steel-4130", "E": 200.*(10**9), "sigma_yield":460*(10**6), "tau_yield": (460./math.sqrt(3))*(10**6),
    "sigma_ult": 560*(10**6), "alpha": 10*(10**-6), "rho":7833.41, "pois":0.33},
    {"name": "ti-6al-4v", "E":110*(10**9), "sigma_yield":900.*(10**6), "rho":4500., "pois":0.33}
             
]



