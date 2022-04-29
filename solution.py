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
