#!/usr/bin/env python3
from fib import fib_py
from  fib_numba import fib_numba
from person import Person
from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np

def main():
    t = np.arange(30,40,1)
    timelst_cc = []
    timelst_py = []
    timelst_nu = []
    for n in range(30,40):
        t1_start = perf_counter()
        f = Person(n)
        f_cc = f.fib()
        t1_stop = perf_counter()
        timelst_cc.append(t1_stop-t1_start)
        
        'python'
        t2_start = perf_counter()
        f_py = fib_py(n)
        t2_stop = perf_counter()
        timelst_py.append(t2_stop-t2_start)
        
        'numba'
        t3_start = perf_counter()
        f_py = fib_numba(n)
        t3_stop = perf_counter()
        timelst_nu.append(t3_stop-t3_start)
        
        # print('cc: ', f_cc)
        # print('time for cc = ', t1_stop-t1_start)
        # print('python: ', fib_py(n))
        # print('time for py = ', t2_stop-t2_start)
        # print('numba: ', fib_numba(n))
        # print('time for nu = ', t3_stop-t3_start)
    plt.plot(t,timelst_cc,'r--', label = 'C++')
    plt.plot(t,timelst_nu,'bs', label = 'numba')
    plt.plot(t,timelst_py,'g^', label = 'python')
    plt.ylabel('time')
    plt.xlabel('n')
    plt.show()
    plt.savefig("fib_plt.png")

if __name__ == '__main__':
	main()