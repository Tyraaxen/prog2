# Date  2023-10-12
# Rewied by: Naser Shabani
# Email: tyra_axen@hotmail.se

import math
import random
import matplotlib.pyplot as plt
import numpy as np

def Pi_hyper(n,d):
    
    sum_lst=[]
    
    for i in range(n):
        sum = 0
        x_lst = [random.uniform(-1,1) for i in range(d)] #list comprehension
        
        for i in x_lst:
            sum += i**2
            
        sum_lst.append(sum)
        
    sum_filtered = list(filter(lambda x: x<=1, sum_lst)) #filter and lambda
    n_c = len(sum_filtered)

    pi_exact = math.pi
    V_approx = (2**d)*n_c/n
    print('approximated Volume for n =',n,'and d =',d,':', V_approx)
    #print('n_c: ', n_c)
    an_sol = math.pi**(d/2)/math.gamma((d/2) + 1)
    print('analytical solution: ', an_sol)
    
    return pi_exact

Pi_hyper(100000,2)
Pi_hyper(100000,11)