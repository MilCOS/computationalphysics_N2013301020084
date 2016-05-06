import math
import easygui
from visual import *
import matplotlib.pyplot as pl

class States:

    def __init__(self, ball=sphere(pos=vector(0,0,0),radius=0.5), t=0):
        self.t = t
        self.x = ball.pos.x
        self.z = ball.pos.z
        self.y = ball.pos.y
        self.vx = ball.velocity.x
        self.vz = ball.velocity.z
        self.vy = ball.velocity.y
        self.v = mag(ball.velocity)
        self.d = mag(ball.pos)

class Pendulum:
        
    def __init__(self, _sta = States(), gummy = sphere(pos=vector(0,0,0),radius=0.5), d_t=0.01):
        self.states = []
        self.states.append(_sta)
        self.dt = d_t
        self.keys = self.choosemode()
        self.modes = Choosemode(gummy)
        self.gummy = gummy
    def Next(self):
        [key_0,key_1] = self.keys
        states_t = self.states[-1]
        
        add = []
        if key_0 == 'NotRotate': 
            add = add + self.modes.NotRotate(states_t, self.dt)
        if (key_0 == 'Rotate')and(states_t.d +states_t.r >= 50):
            add = add + self.modes.Rotate(states_t, self.dt)
        if key_1 == 'Rigid': 
            add = add + self.modes.Rigid(states_t, self.dt)
        if key_1 == 'Coulomb': 
            add = add + self.modes.Coulomb(states_t, self.dt)
        [vx,vy,vz] = [states_t.vx, states_t.vy, states_t.vz] + add_v
        [vx,vy,vz] = judge()
        [x,y,z] = [states_t.x,states_t.y,states_t.z] + [vx,vy,vz] * self.dt
        t = states_t.t + self.dt
        stat = [x,y,z]+[vx,vy,vz]
        velo = collid(stat)
        ball_t = sphere(pos=vector(x,y,z),radius=0.5,color=color.white)
        ball_t.velocity = vector(vx,vy,vz)
        #---------
        self.states.append(States(ball_t, states_t.t+self.dt))
        return [ball_t, self.gummy, t]

    def choosemode(self):
        key_0 = easygui.buttonbox('Choose the small angle approximation or not','CHOOSE',['NotRotate', 'Rotate'])
        key_1 = easygui.buttonbox('Choose whether to add the damping force or not','CHOOSE',['Rigid','Coulomb'])
        return [key_0,key_1]

    def path(self):
        states_t = self.states[-1]
        [x,y,z] = [states_t.x,states_t.y,states_t.z]
        return sphere(pos=vector(x,y,z), radius=0.04, color=color.white)

    def judge(self):
        states_t = self.states[-1]
        [x,y,z] = [states_t.x,states_t.y,states_t.z]
        r = states_t.r
        [vx,vy,vz] = [states_t.vx,states_t.vy,states_t.vz]
        if (abs(x)-r) <=10 return [-vx,vy,vz]
        if (abs(y)-r) <=10 return [vx,-vt,vz]
        if (abs(z)-r) <=10 return [vx,vy,-vz]
        if (states_t.d >=50):
           tempvec = norm(vector(states_t.x,states_t.y,states_t.z))
           velo = vector(states_t.vx,states_t.vy,states_t.vz)
           temp = 2 * dot(tempvec,velo)
           velo = velo - temp * tempvec
           return velo
        return [vx,vy,vz]

    def collid(self, stat=[0,0,0,0,0,0]):
        [x,y,z,vx,vy,vz]=stat
        pos = vector(x,y,z)
        velo = vector(vx,vy,vz)
        if mag(pos - gummy.pos) <= 2*self.gummy.radius:
            temp = velo
            velo = gummy.velocity
            self.gummy.velocity = temp 
            return velo
        else return False

class Choosemode:
    def __init__(self, gummy=sphere(vector(0,0,0),radius=0.5)):
        self.q = para[0]
        self.omega_D = para[1]
        self.FD = para[-1]
        self.gummy = gummy

    def NotRotate(self, states_t, dt):
        d_v = 0
        return d_v

    def Rotate(self, states_t, dt):
        temppos_t = vector(states_t.x,states.y,states_t.z)
        omega = vector(0,2,0) # angular velocity to cause the shift!
        
        d_v = cross(omega,temppos_t)
        return d_v

    def Rigid(self, states_t, dt):
        d_v = 0
        return d_v

    def Coulomb(self, states_t, dt):
        temppos_t = vector(states_t.x,states.y,states_t.z)
        distance = mag(self.gummy - temppos_t)
        d_v = 0.1 * temppos_t * (distance)^(-3) * dt
        return d_v

# ----------


