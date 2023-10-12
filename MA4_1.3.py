# Date  2023-10-12
# Rewied by: Naser Shabani
# Email: tyra_axen@hotmail.se

import math
import random

import concurrent.futures as futures
from time import perf_counter as pc

def Pi_hyper(n,d=11):
    
    sum_lst=[]
    
    for i in range(n):
        sum = 0
        x_lst = [random.uniform(-1,1) for i in range(d)] #list comprehension
        
        for i in x_lst:
            sum += i**2
            
        sum_lst.append(sum)
        
    sum_filtered = list(filter(lambda x: x<=1, sum_lst)) #filter and lambda
    n_c = len(sum_filtered)
    V_approx = (2**d)*n_c/n
    #print('approximated Volume: ', V_approx)
    an_sol = math.pi**(d/2)/math.gamma((d/2) + 1)
    #print('analytical solution: ', an_sol)
    
    return V_approx

def Pi_hyper_paralell(n,d=11,num_processes=10):
    
    points = n // num_processes
    p = [points for i in range(num_processes)]
    # Kompensera för ojämna n
    p[0] += n % num_processes
    
    with futures.ProcessPoolExecutor() as ex:
        results = ex.map(Pi_hyper, p)
    #for r in results:
    #    print('result: ', r)
    return sum(results)/num_processes

if __name__ == '__main__':
    t1_start = pc()
    print('approximated volume for hyper_paralell:', Pi_hyper_paralell(10000000,11)) 
    t1_stop = pc()
    print('time for hyper_paralell:', t1_stop-t1_start,'seconds')
    
    t2_start = pc()
    print('approximated volume for hyper:', Pi_hyper(10000000,11))
    t2_stop = pc()
    print('time for hyper:', t2_stop-t2_start,'seconds')
    
    