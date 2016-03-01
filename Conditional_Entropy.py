# tykimoss_20160213

import numpy as np
import math

# Algorithm 1 Linear_Regression_Traninig(y, X, eta, limit)

#pxy = np.array([[1./8., 3./8.],
#               [1./16., 3./16.],
#               [1./16., 1./16.],
#               [1./16, 1./16.]])
#

"""
4   AA
3   AAAABBBB
2   BB
1   AABB
    
"""
pxy = np.array([[1./8., 0.],
                [1./4., 1./4.],
                [0., 1./8.],
                [1./8., 1./8.]])

px = np.zeros(pxy.shape[1])
py = np.zeros(pxy.shape[0])
Hcyx = 0
Hjxy = 0
Hx = 0
Hy = 0

for xi in range(0, pxy.shape[1]):
    for yi in range(0, pxy.shape[0]):
        px[xi] = px[xi] + pxy[yi][xi]
        py[yi] = py[yi] + pxy[yi][xi]

for yi in range(0, pxy.shape[0]):
    for xi in range(0, pxy.shape[1]):
        py[yi] = py[yi] + pxy[yi][xi]

print "p(x) : " + str(px)
print "p(y) : " + str(py)

for xi in range(0, pxy.shape[1]):
    for yi in range(0, pxy.shape[0]):
        if not pxy[yi][xi] == 0 :
            Hjxy = Hjxy - pxy[yi][xi] * math.log(pxy[yi][xi],2)

print "H(X,Y) : " + str(Hjxy)

for xi in range(0, pxy.shape[1]):
    Hx = Hx - px[xi] * math.log(px[xi],2)

print "H(X) : " + str(Hx)

for xi in range(0, pxy.shape[1]):
    for yi in range(0, pxy.shape[0]):
        if not pxy[yi][xi] == 0 :
            Hcyx = Hcyx - pxy[yi][xi] * math.log((pxy[yi][xi])/px[xi],2)

print "H(Y|X) : " + str(Hcyx)

print "H(X,Y) - H(X) : " + str(Hjxy-Hx)