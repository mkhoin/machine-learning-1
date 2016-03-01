# tykimoss_20160213

import numpy as np
import math

# Algorithm 1 Linear_Regression_Traninig(y, X, eta, limit)

px = np.array([1./2., 1./4., 1./8., 1./8.])

H = 0

for pxi in px:
    print pxi
    H = H - pxi * math.log(pxi,2)

print H
