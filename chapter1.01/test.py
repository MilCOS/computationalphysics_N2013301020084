from visual import *
import math

scene.autoscale=0
scene.range=(22,6,22)
scene.title="Battle Field Online"

# The Battlefield...
earth = box(pos=vector(0,0,0),length=20,height=1,width=20,color=color.blue)

# Position of our base and the bomb
base=sphere(pos=vector(0,0.25,0),radius=1,color=color.black)
bomb=sphere(pos=vector(0,1,0),radius=0,color=color.white)
r_bomb=float(raw_input('Please give the size(cm) of the bomb: '))
print '-------------------------------'
bomb.radius=r_bomb/100
bomb.mass=float(raw_input("Choose the mass(kg) of the bomb, though it's irrelevant for now: "))
print '-------------------------------'

# Randomly choose the target position
t_x = random.uniform(-7,7) 
t_z = random.uniform(-7,7)
t_h = random.uniform(0,4) 
t_r = random.uniform(0.1,1.5)
target = cone(pos=(t_x,0.5,t_z), axis=(0,t_h,0), radius=t_r,color=color.red)
print 'Target information: '
print 'position',target.pos
print 'effective radius',target.radius
print 'horizontal distance',mag(target.pos)*100
print '-------------------------------'
print 'You must destroy it on the first shot!'
# Initail velocity direction
(x,h,z)=target.pos
angle=raw_input('Please give the firing angle(degree): ')
angle=float(angle)/180*math.pi
h = math.tan(angle)*(x**2+z**2)**0.5
velo=norm(vector(x,h,z))
arow = cone(pos=(0,1,0), axis=velo*3, radius=0.1,color=color.red)
print 'Firing direction:',velo
print '-------------------------------'

# Initail velocity magnitude
magni=float(raw_input('Ordering the bombarding strength(cm/s): '))
print '-------------------------------'
bomb.momentum=velo*magni*bomb.mass/100
bomb.velocity=velo*magni/100
print bomb.velocity
print '-------------------------------'
(a,b,c)=bomb.pos

# Rules to judge & Comments
distance1=t_h
distance2=t_r+bomb.radius
print distance1,distance2 #debugging
char1='Target has been destroyed!'
char2='Missed!'
dt=0.01
counter=1
hat = 0 #debugging

# Variety of the bomb
while 1:
    rate(100) #refresh rate at every second
    bomb.pos=bomb.pos+bomb.velocity*dt
    if  bomb.pos.y < bomb.radius: #Bouncing back
        bomb.velocity.y = abs(bomb.velocity.y)
        counter+=1
    if  bomb.pos.y >= bomb.radius:
        bomb.velocity.y = bomb.velocity.y - 9.8*dt #Newton's Second Law
    if  abs(bomb.pos.x-target.pos.x) <= t_r and abs(bomb.pos.z-target.pos.z) <= t_r and bomb.pos.y<=distance1 : # At the first time hit on the target's axie or not
        hat+=1
        print(hat) #debugging
        if (counter==1): # Didn't miss at the first time 
            print char1
            break 
        else: # Missed at the first time
            print char2  
            break 
    if  mag(bomb.pos-target.pos)<=distance2 and bomb.pos.y<= t_h : # At the first time hit on the target's range or not
        hat+=2
        print(hat) #debugging
        if (counter==1): # Didn't miss at the first time 
            print char1
            break 
        else: # Missed at the first time
            print char2
            break 
    if  2*abs(bomb.pos.x)>earth.length or 2*abs(bomb.pos.z)>earth.width : #Out of range
        counter+=3
        print(hat) #debugging
        print char2 
        break 
# Enjoy!







#This 99th floor is mine!!!
