#!/usr/bin/env python3
from fib import fib_py
from  fib_numba import fib_numba
from person import Person

def main():
	n = 20
	f = Person(5)
	print(f.get())
	f.set(n)
	print(f.get())
	print('cc: ', f.fib())
	print('python: ', fib_py(n))
	print('numba: ', fib_numba(n))

if __name__ == '__main__':
	main()
