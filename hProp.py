'''
This code investigates the proportionality of the truncation error and h. It
will calculate the maximum global error for several values of h, each time
integrating out to the same value of t. It will then plot the maximum error as a
function of h.
'''

# Perform necessary imports.

import math
import sys
import numpy as np
import matplotlib.pyplot as mpl

# Define a function to calculate position and velocity for each time step using
# the explicit Euler method.

def errCalculate(x0, v0, t, h):

    ti = 0
    xi = x0
    vi = v0
    errArr = np.empty((0, 2), float)

    while ti <= t:
        xAn = v0 * math.sin(ti)
        vAn = v0 * math.cos(ti)
        xErr = xAn - xi
        vErr = vAn - vi
        errArr = np.append(errArr, np.array([[ti, xErr]]), axis=0)
        Xiplus = xi + (h * vi)
        Viplus = vi - (h * xi)
        ti += h
        xi = Xiplus
        vi = Viplus

    fileData = np.savetxt('hPropData.txt', errArr)    
    return errArr

# Define function to get the error array for each value of h and find the
# maximum error.

def hErrs(x0, v0, t):
    h0 = t/10000
    hErrsArr = np.empty((0, 2), float)

    h0Errs = errCalculate(x0, v0, t, h0)
    errMax0 = 0
    for item in h0Errs:
        if item[1] > errMax0:
            errMax0 = item[1]
    hErrsArr = np.append(hErrsArr, np.array([[h0, errMax0]]), axis=0)

    h02Errs = errCalculate(x0, v0, t, (h0/2))
    errMax2 = 0
    for item in h02Errs:
        if item[1] > errMax2:
            errMax2 = item[1]
    hErrsArr = np.append(hErrsArr, np.array([[(h0/2), errMax2]]), axis=0)

    h04Errs = errCalculate(x0, v0, t, (h0/4))
    errMax4 = 0
    for item in h04Errs:
        if item[1] > errMax4:
            errMax4 = item[1]
    hErrsArr = np.append(hErrsArr, np.array([[(h0/4), errMax4]]), axis=0)

    h08Errs = errCalculate(x0, v0, t, (h0/8))
    errMax8 = 0
    for item in h08Errs:
        if item[1] > errMax8:
            errMax8 = item[1]
    hErrsArr = np.append(hErrsArr, np.array([[(h0/8), errMax8]]), axis=0)

    h016Errs = errCalculate(x0, v0, t, (h0/16))
    errMax16 = 0
    for item in h016Errs:
        if item[1] > errMax16:
            errMax16 = item[1]
    hErrsArr = np.append(hErrsArr, np.array([[(h0/16), errMax16]]), axis=0)

    return hErrsArr


# Define function to graph maximum position error as functions of h.

def hErrGrapher(hErrsArr):
    mpl.plot(hErrsArr[:, 0], hErrsArr[:, 1])
    mpl.show()

if __name__ == '__main__':
    x0 = float(sys.argv[1])
    v0 = float(sys.argv[2])
    t = float(sys.argv[3])

    truncErrs = hErrs(x0, v0, t)
    hErrGrapher(truncErrs)
