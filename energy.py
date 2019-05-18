'''
This code numerically investigates the evolution of the total normalized energy
of a mass on a spring as a function of time. The energy is also plotted as a
function of time.
'''

# Perform necessary imports.

import math
import sys
import numpy as np
import matplotlib.pyplot as mpl

# Define a function to calculate position, velocity, and energy for each time
# step using the explicit Euler method.

def enCalculate(x0, v0, t):

    h = float(t)/100000
    ti = 0
    xi = x0
    vi = v0
    enArr = np.empty((0, 2), float)

    while ti <= t:
        ei = xi**2 + vi**2
        enArr = np.append(enArr, np.array([[ti, ei]]), axis=0)
        Xiplus = xi + (h * vi)
        Viplus = vi - (h * xi)
        ti += h
        xi = Xiplus
        vi = Viplus

    fileData = np.savetxt('energyData.txt', dataSeq)    
    return enArr

# Define functions to graph energy as a function of time.

def enGrapher(enArr):
    mpl.plot(enArr[:, 0], enArr[:, 1])
    mpl.show()

if __name__ == '__main__':
    x0 = float(sys.argv[1])
    v0 = float(sys.argv[2])
    t = float(sys.argv[3])

    energy = enCalculate(x0, v0, t)
    enGrapher(energy)
