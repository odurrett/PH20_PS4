'''
This code calculates and plots x(t) vs. v(t) to examine the phase space of the
analytic solution.
'''

# Perform necessary imports.

import math
import sys
import numpy as np
import matplotlib.pyplot as mpl

# Define a function to calculate position and velocity for each time step using
# the analytic solution.

def posVelCalculate(x0, v0, t):

    h = float(t)/1000
    ti = 0
    xi = x0
    vi = v0
    posVelArr = np.empty((0, 3), float)

    while ti <= t:
        x = v0 * math.sin(ti)
        v = v0 * math.cos(ti)
        posVelArr = np.append(posVelArr, np.array([[ti, x, v]]), axis=0)
        ti += h

    fileData = np.savetxt('anPhaseData.txt', dataSeq)    
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
