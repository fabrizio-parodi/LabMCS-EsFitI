from   iminuit import Minuit
import numpy as np

def f(x,a,b):
    return a*x+b
def chi2(a,b):
    val = 0
    for i in range(0,len(x)):
        val = val + ((y[i]-f(x[i],a,b))/ey[i])**2
    return val
x  = np.array([]); y  = np.array([]); ex = np.array([]); ey = np.array([])
for line in open("pendolo.dat"):
    dt  = line.split() 
    if len(dt)!=4:
        continue
    x   = np.append(x,  float(dt[0])); y   = np.append(y,  float(dt[1]))
    ex  = np.append(ex, float(dt[2])); ey  = np.append(ey, float(dt[3]))

