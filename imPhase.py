'''
This code calculates and plots x(t) vs. v(t) to examine the phase space of the
implicit Euler method.
'''

# Perform necessary imports.

import math
import sys
import numpy as np
import matplotlib.pyplot as mpl

# Define a function to calculate position and velocity for each time step using
# the implicit Euler method.

def posVelCalculate(x0, v0, t):
    
    h = float(t)/1000
    ti = 0
    xi = x0
    vi = v0
    posVelArr = np.empty((0, 3), float)
    
    while ti <= t:
        posVelArr = np.append(posVelArr, np.array([[ti, xi, vi]]), axis=0)
        Xiplus = (xi + (h * vi))/(1 + h**2)
        Viplus = ((-xi * h) + vi)/(1 + h**2)
        ti += h
        xi = Xiplus
        vi = Viplus
        
    return posVelArr

# Define a function to graph position vs. velocity.

def posVelGrapher(posVelArr):
    mpl.plot(posVelArr[:, 1], posVelArr[:, 2])
    mpl.show()
    
if __name__ == '__main__':
    x0 = float(sys.argv[1])
    v0 = float(sys.argv[2])
    t = float(sys.argv[3])
    
    posVel = posVelCalculate(x0, v0, t)
    posVelGrapher(posVel)