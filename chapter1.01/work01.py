from visual import *
import matplotlib.pyplot as plt

scene.autoscale=0
scene.range=(12,12,20)
scene.title="Battle Field Online"
floor = box (pos=(0,0,0), length=4, height=0.5, width=6, color=color.blue)
ball=sphere(pos=vector(0,4,0),radius=0.5,color=color.green)
ball.velocity = vector(0,-1,0)
dt = 0.01
t=0
while 1:
    rate (100)
    ball.pos = ball.pos + ball.velocity*dt
    if ball.y < ball.radius:
        ball.velocity.y = abs(ball.velocity.y)
    else:
        ball.velocity.y = ball.velocity.y - 9.8*dt
        if t == 1000 and t == 2:    
            break
        if t > 1300:
            
            
            if t == 1400:
                print '=='
                break
    t+=10
