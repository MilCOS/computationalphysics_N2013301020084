from scipy.optimize import leastsq
import numpy as np
from matplotlib import pyplot as plt
def func(x, p):
    """
    function for myfit
    """
    tau = p
    return x**tau
def residuals(p, y, x):
    return np.log10(y) - np.log10(func(x, p))
def myfit(x, y):
    p0 = -1.0 
    plsq = leastsq(residuals, p0, args=(y, x)) 
    return plsq

#x = np.arange(1e0,1e3)
#y = (x)**(-2.)
#print(y)
#fit = myfit(x,y)
#fig, ax = plt.subplots()
#ax.set_xscale("log")
#ax.set_yscale("log")
#print(fit[0])
#ax.plot(x, func(x, fit[0]))
#plt.show()
