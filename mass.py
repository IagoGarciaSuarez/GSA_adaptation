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

Purpose: Defining mass calculation function
"""
import numpy 

def mass_calculation(fit, n_agents, mass):
    # For minimization problems, worst value is the highest, best is the lowest
    worst = max(fit)
    best = min(fit)   
        
    if worst == best: # If first iteration, initialize to lowest mass.
        mass = numpy.ones(n_agents)        
        for agent in range(0, n_agents):
           mass[agent] = (fit[agent]-worst)/(best-worst)
            
    mass_sum = sum(mass)
    for agent in range(0, n_agents):
        mass[agent] = mass[agent]/mass_sum # Updates each agent's mass based on its fitness
            
    return mass
