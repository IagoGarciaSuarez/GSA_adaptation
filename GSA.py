# -*- coding: utf-8 -*-
"""
Python code of Gravitational Search Algorithm (GSA)
Reference: Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm." 
           Information sciences 179.13 (2009): 2232-2248.	
Coded by: Iago G. S. (iago.garcia.suarez.ds@gmail.com)

This code is an adaptation with educational purposes and is strongly based on 
            this implementation from Esmat Rashedi in Matlab: https://www.mathworks.com/matlabcentral/fileexchange/27756-gravitational-search-algorithm-gsa

Purpose: Main file of Gravitational Search Algorithm(GSA) 
            for minimizing of the Objective Function
"""
import numpy
import time
from solution import Solution
from mass import mass_calculation
from g_const import g_const_calculation
from g_field import g_field_calculation
from move import move

def GSA (n_agents, max_value, min_value, n_dims, max_iters, obj_func):
    sol = Solution(n_agents, max_value, min_value, n_dims, max_iters, obj_func.__name__)
    # Initializations
    velocity = numpy.zeros((n_agents, n_dims)) # Velocity for any agent in any dimension
    fit = numpy.zeros(n_agents) # Fitness value for any agent
    mass = numpy.ones(n_agents) # Mass value for any agent
    pos = numpy.random.uniform(0, 1, (n_agents, n_dims)) *(max_value - min_value) + min_value # Random positions for agents
    convergence_curve = numpy.zeros(max_iters) 
    best_score = float("inf") # Initial best value is infinity (minimization problem)

    print(f"GSA is searching for the optimal values for '{obj_func.__name__}'")

    timer_start = time.time()
    sol.start_time = timer_start

    for iter in range(0, max_iters):
        for agent in range(0, n_agents):
            pos[agent, :] = numpy.clip(pos[agent, :], min_value, max_value) # Set agent position to valid values
            # Fitness calculation for each particle
            fit[agent] = obj_func(pos[agent, :])
            
            # If agent fitness is better than the best score, update it
            if fit[agent] < best_score:
                best_score = fit[agent]

        # Mass calculation
        mass = mass_calculation(fit, n_agents, mass)

        # Update gravitational constant
        g_const = g_const_calculation(iter, max_iters)

        # Calculation of the gravitational field
        acceleration = g_field_calculation(n_agents, n_dims, pos, mass, iter, max_iters, g_const)

        # Update agent position and velocity
        pos, velocity = move(n_agents, n_dims, pos, velocity, acceleration)

        convergence_curve[iter] = best_score
        
        print(f'\nIteration: {iter + 1}/{max_iters}\nBest fitness: {best_score}\n')
    timer_end = time.time()  
    sol.end_time = time.strftime("%H:%M:%S - %d/%m/%Y")
    sol.execution_time = timer_end - timer_start
    sol.convergence = convergence_curve
    print('---------------------------- END --------------------------------')
    return sol