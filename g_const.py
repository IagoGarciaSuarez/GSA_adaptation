# -*- coding: utf-8 -*-
"""
Python code of Gravitational Search Algorithm (GSA)
Reference: Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm." 
           Information sciences 179.13 (2009): 2232-2248.	
Coded by: Iago G. S. (iago.garcia.suarez.ds@gmail.com)
Original code authors:  Mukesh Saraswat (saraswatmukesh@gmail.com), 
                        Himanshu Mittal (emailid: himanshu.mittal224@gmail.com)
                        Raju Pal (emailid: raju3131.pal@gmail.com)
This code is an adaptation with educational purposes and is strongly based on 
            this implementation: https://github.com/himanshuRepo/Gravitational-Search-Algorithm.git

Purpose: Defining the Gravitational Constant calculation function
"""

import numpy

def g_const_calculation(iter, n_iters):
    alfa = 20
    g_0 = 100
    variation = numpy.exp(-alfa*float(iter)/n_iters) # Updates the constant so the latter in the loop, the lower the constant
    return g_0*variation
    