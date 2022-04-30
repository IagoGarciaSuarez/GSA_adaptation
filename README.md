# Gravitational Search Algorithm Adaptation

Reference: Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm.", Information sciences 179.13 (2009): 2232-2248.

Python adaptation from Gravitational Search Algorithm (GSA) implementation in Matlab by Esmat Rashedi

Coded by: Iago G. S. (iago.garcia.suarez.ds@gmail.com)

This code is an adaptation with educational purposes and is strongly based on this implementation from Esmat Rashedi in Matlab: 
<https://www.mathworks.com/matlabcentral/fileexchange/27756-gravitational-search-algorithm-gsa>

## Installation Guide

To clone the repository, go to the desired directory using the terminal and run:

```sh
git clone git@github.com:IagoGarciaSuarez/GSA_adaptation.git
```

Once cloned, go inside the cloned directory and run:

```sh
pip install -r requirements.txt
```

## User guide

The implementation is specific for minimization problems.
Each part of the GSA is explained within the code. For custom parameters, edit `benchmark.py`.
Once the parameters are set, the algorithm can be tested using:

```sh
python benchmark.py
```
