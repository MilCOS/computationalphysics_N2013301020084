from visual import *
import math
import easygui

scene.autoscale=0
scene.range=(220,10,220)
scene.title="Battle Field Online"

def path(l=0,h=0):
    x = l * (target.pos.x/mag(target.pos))
    z = l * (target.pos.z/mag(target.pos))
    return sphere(pos=vector(x,h,z), radius=0.5, color=color.red)

# The Battlefield...
earth = box(pos=vector(0,0,0),length=200,height=1,width=200,color=color.blue)

# Position of our base and the bomb
base=sphere(pos=vector(0,0.25,0),radius=1,color=color.black)
bomb=sphere(pos=vector(0,1,0),radius=0,color=color.white)
r_bomb=float(easygui.enterbox('Please give the size(m) of the bomb','Initialise Bomb'))
print '-------------------------------'
bomb.radius=r_bomb
bomb.pos.y=r_bomb
bomb.mass=float(easygui.enterbox("Choose the mass(kg) of the bomb, though it's irrelevant for now: ",'Initialise Bomb'))
print '-------------------------------'

# Randomly choose the target position
t_r = 0; t_x = 0; t_z = 0
if (t_r) < math.sqrt((t_x)**2+(t_z)**2)+bomb.radius:
    t_x = random.uniform(-90,90) 
    t_z = random.uniform(-90,90)
    t_h = random.uniform(1,6) 
    t_r = random.uniform(1,5)
    target = cone(pos=(t_x,0.5,t_z), axis=(0,t_h,0), radius=t_r,color=color.red)
easygui.msgbox('Position: '+str(target.pos)+'\nEffective radius '+str(target.radius)+'\nHorizontal distance'+str(mag(target.pos)),'Target information')
print '-------------------------------'

easygui.msgbox('You must destroy it on the first shot!','Warning')

# Initail velocity direction
(x,h,z)=target.pos
angle=float(easygui.enterbox('Please give the firing angle(degree): '+'\nTarget Position: '+str(target.pos)+'\nEffective radius '+str(target.radius)+'\nHorizontal distance'+str(mag(target.pos)),'Initialise Bomb(Angle)'))
angle=math.radians(angle)
h = math.tan(angle)*(x**2+z**2)**0.5
velo=norm(vector(x,h,z))
arrow = cone(pos=(0,1,0), axis=velo*(bomb.radius+3), radius=0.1,color=color.red)
easygui.msgbox('Firing direction:'+str(velo),'Information')
print '-------------------------------'

# Initail velocity magnitude
magni=float(easygui.enterbox('Ordering the bombarding strength(m/s): '+'\nTarget Position: '+str(target.pos)+'\nEffective radius '+str(target.radius)+'\nHorizontal distance'+str(mag(target.pos)),'Initialise Bomb(Velocity)'))
print '-------------------------------'
bomb.momentum=velo*magni*bomb.mass
bomb.velocity=velo*magni
easygui.msgbox( str(bomb.velocity),'Information')
print '-------------------------------'
(a,b,c)=bomb.pos

# Rules to judge & Comments
distance1=t_h+bomb.radius
distance2=t_r+bomb.radius
dt=0.01
counter=1
hat = 0 #debugging
note = 1

char1='Target has been destroyed!'
char2='Missed!'
image1 = "twilight_sparkle_win.png"
image2 = "starlight_glimmer_great_shot.png"
def reply(k):
    char1='Target has been destroyed!'
    char2='Missed!'
    image1 = "twilight_sparkle_win.png"
    image2 = "starlight_glimmer_great_shot.png"
    if k == 1:
        easygui.buttonbox(char1, image=image1, choices=['Continue'])
    if k == 2:
        easygui.buttonbox(char2, image=image2, choices=['Continue'])

# Variety of the bomb
while 1:
    rate(100) #refresh rate at every second
    note += 1
    h_bomb = bomb.pos.y
    l_bomb = math.sqrt(bomb.pos.x**2+bomb.pos.z**2)
    bomb.pos=bomb.pos+bomb.velocity*dt
    if  note % 10 == 0 or note == 1: path(l_bomb,h_bomb)
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
            reply(1)
            break 
        else: # Missed at the first time
            print char2  
            reply(2)
            break 
    if  mag(bomb.pos-target.pos)<=distance2 and bomb.pos.y<= distance1 : # At the first time hit on the target's range or not
        hat+=2
        print(hat) #debugging
        if (counter==1): # Didn't miss at the first time 
            print char1
            reply(1)
            break 
        else: # Missed at the first time
            print char2
            reply(2)
            break 
    if  2*abs(bomb.pos.x)>earth.length or 2*abs(bomb.pos.z)>earth.width : #Out of range
        counter+=3
        print(hat) #debugging
        print char2 
        reply(2)
        break 
# Enjoy!







#This 99th floor is mine!!!
