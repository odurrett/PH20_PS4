'''
This code numerically and analytically investigates the motion of a mass on a
spring according to the equation F = -kx. It will calculate the position and
velocity at equally-spaced points for a specified time interval following both
the numerical and analytical methods. It will then calculate and plot the global
errors as a function of time.
'''

# Perform necessary imports.

import math
import sys
import numpy as np
import matplotlib.pyplot as mpl

# Define a function to calculate position and velocity errors for each time
# step.

def errCalculate(x0, v0, t):

    h = float(t)/100000
    ti = 0
    xi = x0
    vi = v0
    errArr = np.empty((0, 3), float)

    while ti <= t:
        xAn = v0 * math.sin(ti)
        vAn = v0 * math.cos(ti)
        xErr = abs(xAn - xi)
        vErr = abs(vAn - vi)
        errArr = np.append(errArr, np.array([[ti, xErr, vErr]]), axis=0)
        Xiplus = (xi + (h * vi))/(1 + h**2)
        Viplus = ((-xi * h) + vi)/(1 + h**2)
        ti += h
        xi = Xiplus
        vi = Viplus

    fileData = np.savetxt('impAbsErrsData.txt', errArr)    
    return errArr

# Define functions to graph position and velocity errors as functions of time.

def errPosGrapher(errArr):
    mpl.plot(errArr[:, 0], errArr[:, 1])
    mpl.show()

def errVelGrapher(errArr):
    mpl.plot(errArr[:, 0], errArr[:, 2])
    mpl.show()

if __name__ == '__main__':
    x0 = float(sys.argv[1])
    v0 = float(sys.argv[2])
    t = float(sys.argv[3])

    errs = errCalculate(x0, v0, t)
    errPosGrapher(errs)
    errVelGrapher(errs)
