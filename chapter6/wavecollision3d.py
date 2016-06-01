from __future__ import print_function
"""
A very simple 'animation' of a 3D plot
"""
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import time


def generate(xs, ys):
    #R = 1 - np.sqrt(X**2 + Y**2)
    Z = np.exp(-k*((xs-x0)**2+(ys-y0)**2))
    for i in range(len(xs)):
        Z[0][i]=0
        Z[-1][i]=0
        Z[i][0]=0
        Z[i][-1]=0
    return Z

def animate():
    global Z1,Z2,pre_Z1,next_Z1,pre_Z2,next_Z2
    for i in range(1,len(xs)-1):
        for j in range(1,len(ys)-1):
            next_Z1[i][j]=2*(1-r1**2)*Z1[i][j]-pre_Z1[i][j]+r1**2*(Z1[i+1][j]+Z1[i-1][j]) - 2*r1**2*Z1[i][j]+r1**2*(Z1[i][j+1]+Z1[i][j-1]) 
            next_Z2[i][j]=2*(1-r2**2)*Z2[i][j]-pre_Z2[i][j]+r2**2*(Z2[i+1][j]+Z2[i-1][j]) - 2*r2**2*Z2[i][j]+r2**2*(Z2[i][j+1]+Z2[i][j-1]) 
    pre_Z1, pre_Z2 = Z1+0, Z2+0 #[z for z in Z1], [z for z in Z2]
    Z1, Z2 = next_Z1+0, next_Z2+0 #[z for z in next_Z1], [z for z in next_Z2]
#    for i in range(len(xs)):
#        Z1[0][i]=0
#        Z1[-1][i]=0
#        Z1[i][0]=0
#        Z1[i][-1]=0
#    for i in range(len(xs)):
#        Z2[0][i]=0
#        Z2[-1][i]=0
#        Z2[i][0]=0
#        Z2[i][-1]=0



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

c1, c2 = 300, 150
_dx = 0.01
_dy = 0.01
_dt = _dx / c1
k = 1000
r1 = c1 * _dt/_dx #_dx=_dy
r2 = c2 * _dt/_dx #_dx=_dy

xs = np.arange(0, 1, _dx)
ys = np.arange(0, 1, _dy)
#xs = np.linspace(-1, 1, 50)
#ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)
x0, y0 = 0.3, 0.3
Z1 = generate(X,Y)
pre_Z1 = generate(X, Y)
next_Z1 = generate(X, Y)
x0, y0 = 0.5, 0.5
Z2 = generate(X,Y)
pre_Z2 = generate(X, Y)
next_Z2 = generate(Y, Y)

wframe = None
tstart = time.time()
k = 0
for t in np.linspace(0, 1, 200):

    oldcol = wframe
    animate()
    #Z = [[Z1[i][j]+Z2[i][j] for i in range(len(X))]for j in range(len(Y))]
    Z = np.add(Z1,Z2)
    wframe = ax.plot_wireframe(X, Y, Z2, rstride=2, cstride=2)
#    cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
#    cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
#    cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

    # Remove old line collection before drawing
    if oldcol is not None:
        ax.collections.remove(oldcol)
    k += 1
    plt.pause(_dt)
print(k)

