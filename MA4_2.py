#!/usr/bin/env python3
from fib import fib_py
from person import Person

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print('hej')
	print('cc: ', f.fib_cc())
	print('python: ', fib_py(7))

if __name__ == '__main__':
	main()
