from visual import *
import motion
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

boundary_x1 = box(pos=vector(3,0,0),length=0.1,height=6,width=6,color=color.white)
boundary_x2 = box(pos=vector(-3,0,0),length=0.1,height=6,width=6,color=color.white)
boundary_y1 = box(pos=vector(0,3,0),length=6,height=0.1,width=6,color=color.white)
boundary_y2 = box(pos=vector(0,-3,0),length=6,height=0.1,width=6,color=color.white)
boundary_z1 = box(pos=vector(0,0,3),length=6,height=6,width=0.1,color=color.white)
boundary_z1 = box(pos=vector(0,0,-3),length=6,height=6,width=0.1,color=color.white)

electron_1 = sphere(vector=(-6,10,10),radius=2,color=color.green)
electron_2 = sphere(vector=(-10,6,7),radius=2,color=color.red)
electron_1.velocity=vector(0,0.2,0)
electron_2.velocity=vector(0,0,0.2)

counter = 0
x = []
y = []
z = []
electron_1.trail = curve(color=electron_1.color)
electron_2.trail = curve(color=electron_2.color)
twilight = motion.Charge()
force_X = motion.Choosemode()

def update_position(electron_1,electron_2,dt=0.1): # electron_2 is gummy
    electron_1.velocity = twilight.judge(electron_1,electron_2,dt)
    electron_1.velocity = twilight.collid(electron_1,electron_2,dt)
    dv = force_X.Rigid(electron_1,electron_2,dt)
    electron_1.velocity += dv
    electron_1.pos += electron_1.velocity * dt
    return electron_1,electron_2

while True:
    rate(10)
    electron_1.trail.append(pos=electron_1.pos)
    electron_2.trail.append(pos=electron_2.pos)
    [electron_1,electron_2] = update_position(electron_1,electron_2)
    [electron_2,electron_1] = update_position(electron_2,electron_1)
    update_position(electron_1,electron_2)
    x.append(electron_1.pos.x)
    y.append(electron_1.pos.y)
    z.append(electron_1.pos.z)
    counter += 1

print "Hello World!"
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z,c='r',marker='o')
plt.show()
