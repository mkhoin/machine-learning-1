# tykimoss_20160213

import numpy as np

# Algorithm 1 Linear_Regression_Traninig(y, X, eta, limit)

y = np.array([50, 55, 60, 45, 50])

X = np.array([[[1],
               [160]],
              [[1],
               [165]],
              [[1],
               [160]],
              [[1],
               [170]],
              [[1],
               [170]]])

eta = 0.000001; # learning rate

limit = 0.001;

# internal variable

w = np.array([[0],
              [0]])

new_w = np.array([[0],
                  [0]])


diff = 0;
iternation_count = 0

# interation

while True:

    rqrw_sum = np.array([[0],
                         [0]])
    
    for i in range(0, 5):
        rqrw = 2 * (y[i] - np.dot(w.transpose(), X[i])) * (-1*X[i])
        rqrw_sum = rqrw_sum + rqrw

    new_w = w - eta * rqrw_sum

    diff = np.sqrt(np.mean((new_w - w)**2))

    iternation_count = iternation_count + 1

    if diff < limit :
        break
    
    w = new_w

print 'iteration count:' + str(iternation_count)
print w

# Algorithm 2 Linear_Regression_Testing(xi, w)
xi = np.array([[1],[160]])
yi = np.dot(w.transpose(), xi)
print yi

