# -*- coding: utf-8 -*-
"""
Python code of Gravitational Search Algorithm (GSA)
Reference: Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm." 
           Information sciences 179.13 (2009): 2232-2248.	
Coded by: Iago G. S. (iago.garcia.suarez.ds@gmail.com)

This code is an adaptation with educational purposes and is strongly based on 
            this implementation from Esmat Rashedi in Matlab: https://www.mathworks.com/matlabcentral/fileexchange/27756-gravitational-search-algorithm-gsa

Purpose: Defining the move function for position update
"""
import random

def move(n_agents, n_dims, pos, velocity, acceleration):
    for agent in range(0, n_agents):
        for dim in range (0, n_dims):
            random_num = random.random()
            # Updates velocity in the dimension dim with a random weighted velocity added acceleration
            velocity[agent, dim] = random_num * velocity[agent, dim] + acceleration[agent, dim]
            # Position = position + velocity
            pos[agent, dim] = pos[agent, dim] + velocity[agent, dim]
    return pos, velocity