import math
import easygui
from visual import *
import matplotlib.pyplot as pl
ball=sphere(pos=vector(0,0,0),radius=0,velocity=vector(1,1,1))
gummy = sphere(pos=vector(1,1,1),radius=0)

class Charge:
    def __init__(self):
        self.mode = Choosemode()
    def judge(self, ball, gummy,dt=0.1):
        [x,y,z] = ball.pos
        r = ball.radius
        d = mag(ball.pos)
        [vx,vy,vz] = ball.velocity
#        if (abs(x)-r) <=3:
#            return vector(-vx,vy,vz)
#        if (abs(y)-r) <=3:
#            return vector(vx,-vy,vz)
#        if (abs(z)-r) <=3:
#            return vector(vx,vy,-vz)
        if (d >=50):
            tempvec = norm(ball.pos)
            velo = ball.velocity
            temp = 2 * dot(tempvec,velo)
            velo = velo - temp * tempvec + self.mode.Rotate(ball,gummy,dt)
            return velo
        return vector(vx,vy,vz)

    def collid(self, ball, gummy,dt=0.1):
        pos = ball.pos
        velo = ball.velocity
        if mag(pos - gummy.pos) <= 2*gummy.radius:
            line = norm(pos - gummy.pos)
            temp1 = line * dot(line,gummy.velocity-velo)
            temp2 = line * dot(line,velo-gummy.velocity)
            velo += temp1
            gummy.velocity = temp2
        return velo

class Choosemode:

    def Rotate(self, ball, gummy, dt=0.1):
        temppos_t = ball.pos
        omega = vector(0,2,0) # angular velocity to cause the shift!
        
        d_v = cross(omega,temppos_t) * dt
        return d_v

    def Rigid(self, ball, gummy, dt=0.1):
        d_v = vector(0,0,0)
        return d_v

    def Coulomb(self, ball, gummy, dt=0.1):
        temppos_t = ball.pos
        distance = mag(gummy.pos - temppos_t)
        d_v = - 0.001* temppos_t / (distance**(3)) * dt
        return d_v

#def choosekeys():
#    key_0 = easygui.buttonbox('Choose the small angle approximation or not','CHOOSE',['NotRotate', 'Rotate'])
#    key_1 = easygui.buttonbox('Choose whether to add the damping force or not','CHOOSE',['Rigid','Coulomb'])
#    return [key_0,key_1]

# ----------


