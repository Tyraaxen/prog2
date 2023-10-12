# Date  2023-10-12
# Rewied by: Naser Shabani
# Email: tyra_axen@hotmail.se

def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))
    