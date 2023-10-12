# Date  2023-10-12
# Rewied by: Naser Shabani
# Email: tyra_axen@hotmail.se

from numba import njit
@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return(fib_numba(n-1) + fib_numba(n-2))