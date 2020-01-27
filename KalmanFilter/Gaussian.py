#!/usr/bin/env python3
from math import *

def update(mean1,var1,mean2,var2):
    new_mean = 1/(var1+var2)*(var1 * mean2 + var2 * mean1)
    new_var = 1/((1/var1)+(1/var2))
    return [new_mean, new_var]

def predict(mean1,var1,mean2,var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]


'''def f(mu,sigma2,x):
    return 1/sqrt(2.*pi*sigma2)*exp(-.5*(x-mu)**2 / sigma2)
print(f(10.,4.,8.))'''

print(update(10.,4.,12.,4.))
print(predict(10., 4., 12. , 4.))