'''
This code numerically investigates the motion of a mass on a spring according to
the equation F = -kx. It will calculate the position and velocity at equally-
spaced points for a specified time interval. It will also plot position and
velocity as a function of time.
'''

# Perform necessary imports.

import math
import sys
import numpy as np
import matplotlib.pyplot as mpl

# Define a function to calculate position and velocity for each time step using
# the explicit Euler method.

def posVelCalculate(x0, v0, t):

    # Choose an appropriately small value of h.
    h = float(t)/100000
    # Define iterative variables.
    ti = 0
    xi = x0
    vi = v0
    posVelArr = np.empty((0, 3), float)

    while ti <= t:
        posVelArr = np.append(posVelArr, np.array([[ti, xi, vi]]), axis=0)
        # Update x and v by the explicit Euler method.
        Xiplus = xi + (h * vi)
        Viplus = vi - (h * xi)
        # Step the time forward.
        ti += h
        # Reset x and v values to the updated values.
        xi = Xiplus
        vi = Viplus

    return posVelArr

# Define functions to graph position and velocity as functions of time.

def posGrapher(posVelArr):
    mpl.plot(posVelArr[:, 0], posVelArr[:, 1])
    mpl.show()

def velGrapher(posVelArr):
    mpl.plot(posVelArr[:, 0], posVelArr[:, 2])
    mpl.show()

# Define main function to run the code when the script is opened via the
# command line.

if __name__ == '__main__':
    # Define variables used in the calculation function as inputs from the
    # user.
    x0 = float(sys.argv[1])
    v0 = float(sys.argv[2])
    t = float(sys.argv[3])

    # Call the functions to calculate position and velocity values, as well as
    # graph the position and velocity values as functions of time.
    posVel = posVelCalculate(x0, v0, t)
    posGrapher(posVel)
    velGrapher(posVel)
