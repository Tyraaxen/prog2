#!/usr/bin/env python3
from fib import fib_py
from  fib_numba import fib_numba
from person import Person
from time import perf_counter

def main():
    list = [30,35,40,45]
    for n in list:
        t1_start = perf_counter()
        f = Person(n)
        f_cc = f.fib()
        t1_stop = perf_counter()
        
        'python'
        t2_start = perf_counter()
        f_py = fib_py(n)
        t2_stop = perf_counter()
        
        'numba'
        t3_start = perf_counter()
        f_py = fib_numba(n)
        t3_stop = perf_counter()
        
        print('cc: ', f_cc)
        print('time for cc = ', t1_start-t1_stop)
        print('python: ', fib_py(n))
        print('time for py = ', t2_start-t2_stop)
        print('numba: ', fib_numba(n))
        print('time for nu = ', t3_start-t3_stop)

if __name__ == '__main__':
	main()