# -*- coding: utf-8 -*-
"""
Python code of Gravitational Search Algorithm (GSA)
Reference: Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm." 
           Information sciences 179.13 (2009): 2232-2248.	
Coded by: Iago G. S. (iago.garcia.suarez.ds@gmail.com)

This code is an adaptation with educational purposes and is strongly based on 
            this implementation from Esmat Rashedi in Matlab: https://www.mathworks.com/matlabcentral/fileexchange/27756-gravitational-search-algorithm-gsa

Purpose: Showing algorithm execution
"""

import numpy
from GSA import GSA
    
def F1(x):
  """ Spere Function. Global Optimum = 0"""
  res=numpy.sum(x**2)
  return res

obj_func = F1
min_value = -100
max_value = 100
n_dims = 1
n_agents = 25
max_iters = 2500


sol = GSA(n_agents, max_value, min_value, n_dims, max_iters, obj_func)
print(sol)