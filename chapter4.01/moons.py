import matplotlib.pyplot as plt
import math
from visual import *
k = 2.
m = 50
M = m * k
u = m*M/(m+M)
print "u", u
d = 5.

earth = sphere(pos=(0,0,0), radius=5, color=color.white, material=materials.earth)
def reset():
    global moon1,moon2,mc,l1,l2
    moon1 = sphere(pos=(15,0,25), radius=0.5, color=color.white, material=materials.emissive)
    moon2 = sphere(pos=(15,0,20), radius=0.5, color=color.yellow, material=materials.emissive)
    mc = sphere(pos=(0,0,0),radius=0.2, color=color.black)
    mc.pos = (m*moon1.pos+M*moon2.pos)/(m+M)
    print mc.pos
    mc.velocity = vector(10,0,-25)
    l = mag(moon1.pos - moon2.pos)
    l1 = l * M/(m+M)
    l2 = l * m/(m+M)
    moon1.trail = curve(color=moon1.color)
    moon2.trail = curve(color=moon2.color)
def updatePosition(moon1, moon2, omega, theta, t, dt = 0.01):
    # rc = mag(mc.pos)=1
    (xc,yc,zc)=mc.pos
    omega += dt * (-12*math.pi*(xc*math.sin(theta)-zc*math.cos(theta))*(xc*math.cos(theta)+zc*math.sin(theta)))
    theta += omega * dt
    #if (theta <= - math.pi):    theta = theta + 2*math.pi
    #if (theta > math.pi):    theta = theta - 2*math.pi
    e21 = vector(math.cos(theta),0,math.sin(theta))
    moon1.pos = mc.pos + l1 * e21
    moon2.pos = mc.pos - l2 * e21 
    mc.velocity = mc.velocity - (4*math.pi*mc.pos) * dt
    mc.pos += mc.velocity * dt
    t += dt
    return omega,theta,t
s = 0
def run(moon1, moon2, omega, theta, t, dt=0.001):
    counter = 0
    while True:
        rate(1000)
        moon1.trail.append(pos=moon1.pos)
        moon2.trail.append(pos=moon2.pos)
        [i,j,k] = updatePosition(moon1, moon2, omega[-1], theta[-1], t[-1], dt=0.001)
        omega.append(i)
        theta.append(j)
        t.append(k)
        if counter % 1000 == 0:
            print 'Press "q" to plot 3D, or anything else to continue...'
            s = scene.kb.getkey()
            if s == 'Enter' or s == 'q':
                break
            else:
                pass
        counter += 1
    return 'Pinkie'
omega1 = [0]
theta1 = [0.00]
t1 = [0]
reset()
run(moon1, moon2, omega1, theta1, t1, dt=0.0001)
t2 = [0]
omega2 = [0]
theta2 = [0.01]
reset()
run(moon1, moon2, omega2, theta2, t2, dt=0.0001)
theta = theta1
for i in range(len(theta1)):
    theta[i]=abs(theta1[i]-theta2[i])
    if theta[i]==0:
        theta[i] += math.log(-5)
fig = plt.figure()
ax = plt.axes(xlim=(0,max(t1)), ylim=(0.00001,max(theta)*1.1))
plt.semilogy(t1,theta,c='r',marker='.')
plt.xlabel(r'$t(yr)$',fontsize=20)
plt.ylabel(r'$\Delta \theta (radians)$', fontsize=20)
plt.show()
