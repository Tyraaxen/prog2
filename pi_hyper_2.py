import math
import random

import concurrent.futures as futures
from time import perf_counter as pc

def Pi_hyper(n,d=10):
    
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
    print('approximated Volume: ', V_approx)
    #print('n_c: ', n_c)
    an_sol = math.pi**(d/2)/math.gamma((d/2) + 1)
    print('analytical solution: ', an_sol)
    
    return pi_exact

def Pi_hyper_paralell(n,d,num_processes=10):
    #p = [10,10,10,10,10]
    
    points = n // num_processes
    p = [points for _ in range(num_processes)]
    # Compensate for uneven n
    p[0] += n % num_processes
    
    with futures.ProcessPoolExecutor() as ex:
        results = ex.map(Pi_hyper, p)
    for r in results:
        print('result: ', r)
    return sum(results)/d

if __name__ == '__main__':
    Pi_hyper_paralell(10,4)