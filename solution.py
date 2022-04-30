# -*- coding: utf-8 -*-
"""
Python code of Gravitational Search Algorithm (GSA)
Reference: Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm." 
           Information sciences 179.13 (2009): 2232-2248.	
Coded by: Iago G. S. (iago.garcia.suarez.ds@gmail.com)

This code is an adaptation with educational purposes and is strongly based on 
            this implementation from Esmat Rashedi in Matlab: https://www.mathworks.com/matlabcentral/fileexchange/27756-gravitational-search-algorithm-gsa

Purpose: Defining solution format
"""

class Solution:
    def __init__(self, n_agents, max_value, min_value, n_dims, max_iters, obj_func):
        self.obj_func = obj_func
        self.n_agents = n_agents
        self.min_value = min_value
        self.max_value = max_value
        self.n_dims = n_dims
        self.max_iters = max_iters
        self.convergence = []
        self.start_time = 0
        self.end_time = 0
        self.execution_time = 0

    def __str__(self):
        return f'\n\n--------EXECUTION SUMMARY--------\n\n-> GSA PARAMETERS\nObjective function: {self.obj_func}' + \
                f'\nMin value: {self.min_value}\nMax value: {self.max_value}' + \
                f'\nTotal agents: {self.n_agents}\nDimensions: {self.n_dims}\nMax iterations: {self.max_iters}' + \
                f'\n\n-> RESULTS\nExecution time: {self.execution_time}\nFinal value: {self.convergence[-1]}\n\n'