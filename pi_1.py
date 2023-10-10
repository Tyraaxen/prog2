import math
import random
import matplotlib.pyplot as plt
import numpy as np

def Pi(n):
    n_c = 0
    lst_nc_x = []
    lst_nc_y = []
    lst_nk_x = []
    lst_nk_y = []
    for i in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x**2 + y**2 <= 1:
            n_c += 1
            lst_nc_x.append(x)
            lst_nc_y.append(y)
        else:
            lst_nk_x.append(x)
            lst_nk_y.append(y)
        
    plt.plot(lst_nc_x,lst_nc_y, 'ro', lst_nk_x, lst_nk_y, 'bo')
    plt.axis((-1,1,-1,1))
    plt.show()
    
    pi_exact = math.pi
    pi_approx = 4*n_c/n
    print(pi_exact)
    print(pi_approx)
    print(n_c)
    
    return pi_exact

Pi(400)
