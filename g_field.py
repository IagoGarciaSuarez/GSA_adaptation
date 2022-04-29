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

Purpose: Defining the Gravitational Force and acceleration values calculation
"""

import random
import numpy
import math

def g_field_calculation(n_agents, n_dims, pos, mass, iter, n_iters, g_const):
    min_k = 2 # The last iteration will take into account 2 agents for the gravitational force.
    kbest = min_k + (1 - iter/n_iters) * (100 - min_k) # kbest will decrease from total to 2.
    kbest = int(round(n_agents * kbest/100))

    # Sorts masses from highest to lowest
    sorted_masses_index = sorted(range(len(mass)), key=lambda k: mass[k],reverse=True)
    # Initialize force to 0
    force = numpy.zeros((n_agents, n_dims))

    for agent in range(0, n_agents):
        for k in range(0, kbest):
            kb_agent = sorted_masses_index[k]
            eucl_dist = 0
            if kb_agent != agent: # for j in kbest, j != i
                x = pos[agent, :] # Solution found by agent
                y = pos[kb_agent, :] # Solution found by kbest agent
                # Euclidean distance calculation
                esum = 0
                imval = 0
                for dim in range(0, n_dims):
                    imval = ((x[dim] - y[dim])** 2)
                    esum += imval
                eucl_dist = math.sqrt(esum) 
                # Sum of all randomly weighted forces acting on agent
                for dim in range(0, n_dims):
                    rand_num = random.random()
                    force[agent, dim] = force[agent, dim] + rand_num * mass[kb_agent] * mass[agent] * ((pos[kb_agent, dim]-pos[agent, dim])/(eucl_dist+numpy.finfo(float).eps))
    acceleration = numpy.zeros((n_agents, n_dims))
    for agent in range(0, n_agents):
        for dim in range(0, n_dims):
            acceleration[agent, dim] = force[agent, dim] * g_const
    return acceleration