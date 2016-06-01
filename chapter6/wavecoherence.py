from __future__ import print_function
"""
A very simple 'animation' of a 3D plot
Change Z1/Z2/Z at line 77 to plot single wave or wave collision
"""
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import easygui
import time

def generate(xs, ys):
    #R = 1 - np.sqrt(X**2 + Y**2)
    Z = np.exp(-k*((xs-x0)**2))#+(ys-y0)**2))
    for i in range(len(xs)):
        Z[0][i]=0
        Z[0][i]=0
        Z[-1][i]=0
        Z[i][0]=0
        Z[i][-1]=0
    return Z

def animate():
    global Z1,Z2,pre_Z1,next_Z1,pre_Z2,next_Z2
    for i in range(41): #this is where we set blocks
        Z1[i][49]=0
        Z1[-i][49]=0
    for i in range(len(xs)/2-4, len(xs)/2+4):
        Z1[i][49]=0
        
    for i in range(1,len(xs)-1):
        for j in range(1,len(ys)-1):
            next_Z1[i][j]=2*(1-r1**2)*Z1[i][j]-pre_Z1[i][j]+r1**2*(Z1[i+1][j]+Z1[i-1][j]) - 2*r1**2*Z1[i][j]+r1**2*(Z1[i][j+1]+Z1[i][j-1]) 
            next_Z2[i][j]=2*(1-r2**2)*Z2[i][j]-pre_Z2[i][j]+r2**2*(Z2[i+1][j]+Z2[i-1][j]) - 2*r2**2*Z2[i][j]+r2**2*(Z2[i][j+1]+Z2[i][j-1]) 
    pre_Z1, pre_Z2 = Z1+0, Z2+0 #[z for z in Z1], [z for z in Z2]
    Z1, Z2 = next_Z1+0, next_Z2+0 #[z for z in next_Z1], [z for z in next_Z2]

def collect():
    global Z1,pinkie,twily
    temp_p,temp_t = [],[]
    for i in range(len(ys)):
        temp_p.append(i/len(ys))
        temp_t.append(Z1[i][-2])
    pass 



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_xlim(-0.1, 1)
ax.set_ylabel('Y')
ax.set_ylim(0, 1.1)
ax.set_zlabel('Z')
ax.set_zlim(-0.4, 1)

c1, c2 = 300, 150
_dx = 0.01
_dy = 0.01
_dt = _dx / 450
k = 1000
r1 = c1 * _dt/_dx #_dx=_dy
r2 = c2 * _dt/_dx #_dx=_dy

xs = np.arange(0, 1, _dx)
ys = np.arange(0, 1, _dy)
#xs = np.linspace(-1, 1, 50)
#ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)
x0, y0 = 0.3, 0.3
x0 = 0.2
Z1 = generate(X,Y)
pre_Z1 = generate(X, Y)
next_Z1 = generate(X, Y)
x0, y0 = 0.5, 0.5
Z2 = generate(X,Y)
pre_Z2 = generate(X, Y)
next_Z2 = generate(Y, Y)

wframe = None
easygui.ccbox()
tstart = time.time()
k = 0
pinkie,twily=[],[]
for t in np.linspace(0, 1, 400):

    oldcol = wframe
    animate()
    #Z = [[Z1[i][j]+Z2[i][j] for i in range(len(X))]for j in range(len(Y))]
    #Z = np.add(Z1,Z2)
    wframe = ax.plot_wireframe(X, Y, Z1, rstride=2, cstride=2)
#    ax.contourf(X, Y, Z, zdir='z', offset=-0.4, cmap=cm.coolwarm)
#    ax.contourf(X, Y, Z, zdir='x', offset=-0.1, cmap=cm.coolwarm)
#    ax.contourf(X, Y, Z, zdir='y', offset=1.1, cmap=cm.coolwarm)

    # Remove old line collection before drawing
    if oldcol is not None:
        ax.collections.remove(oldcol)

    k += 1
    plt.pause(_dt)
print(k)
plt.show()
