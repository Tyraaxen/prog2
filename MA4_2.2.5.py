#!/usr/bin/env python3
from fib import fib_py
from  fib_numba import fib_numba
from person import Person
from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np

def main():
    t = np.arange(20,30,1)
    timelst_py = []
    timelst_nu = []
    for n in range(20,30):
        
        'python'
        t2_start = perf_counter()
        f_py = fib_py(n)
        t2_stop = perf_counter()
        timelst_py.append(t2_stop-t2_start)
        
        'numba'
        t3_start = perf_counter()
        f_nu = fib_numba(n)
        t3_stop = perf_counter()
        timelst_nu.append(t3_stop-t3_start)
        
    'plots'
    plt.plot(t,timelst_nu, label = 'numba')
    plt.plot(t,timelst_py, label = 'python')
    plt.ylabel('time')
    plt.xlabel('n')
    plt.legend()
    plt.show()
    plt.savefig("fib_pynumba_plt.png")

if __name__ == '__main__':
	main()