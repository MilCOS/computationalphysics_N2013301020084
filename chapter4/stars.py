import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from visual import *
k = 100.
m = 50
M = m * k
u = m*M/(m+M)
print "u", u
d = 100.

earth = sphere(pos=( d*u/m,0,0), radius=5, color=color.white, material=materials.earth)
sun   = sphere(pos=(-d*u/M,0,0), radius=10, color=color.yellow, material=materials.emissive)
v_e = math.sqrt(M/m*u/d)
v_s = -math.sqrt(m/M*u/d)
earth.velocity = vector(0,0.1,0)
sun.velocity = vector(0,-0,0)
earth.trail = curve(color=earth.color)
sun.trail = curve(color=sun.color)


def updatePosition(earth, sun, dt = 0.1):
    d = mag(earth.pos - sun.pos)
    if d < earth.radius+sun.radius:
        d += 1
    earth.velocity += norm(sun.pos-earth.pos) * M/d**2 * dt
    sun.velocity += norm(earth.pos-sun.pos) * m/d**2 * dt
    earth.pos += earth.velocity * dt
    sun.pos += sun.velocity * dt

x_e = []
y_e = []
z_e = []
x_s = []
y_s = []
z_s = []
s = 0
counter = 0
while True:
    rate(1000)
    earth.trail.append(pos=earth.pos)
    sun.trail.append(pos=sun.pos)
    updatePosition(earth, sun)
    if counter % 10 == 0:
        x_e.append(earth.pos.x)
        y_e.append(earth.pos.y)
        z_e.append(earth.pos.z)
        x_s.append(sun.pos.x)
        y_s.append(sun.pos.y)
        z_s.append(sun.pos.z)
    if counter % 500 == 0:
        print 'Press "q" to plot 3D, or anything else to continue...'
        s = scene.kb.getkey()
        if s == 'Enter' or s == 'q':
            break
        else:
            pass
    counter += 1
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_e,y_e,z_e,c='r',marker='o')
ax.scatter(x_s,y_s,z_s,c='b',marker='^')
plt.show()
