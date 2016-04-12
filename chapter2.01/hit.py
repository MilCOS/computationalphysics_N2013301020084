import math
import easygui
from visual import *

def read_readfile():
    
factor = self.readfile()

class states:
    global [a1,a2,vd,delta,]=factor[:]
    def init(ball, t=0):
        self.x = ball.pos.x
        self.z = ball.pos.z
        self.y = ball.pos.y
        self.vx = ball.velocity.vx
        self.vz = ball.velocity.vz
        self.vy = ball.velocity.vy
        self.t = t
        self.v = mag(ball.velocity)

class baseball:
    global [a1,a2,vd,delta,] = factor[:]
    def init(self, init_sta = states(), d_t=0.01):
        self.states = []
        self.states.append(sta)
        self.dt = d_t
        
    def Next(self):
        states_t = self.states[-1]
        x = states_t.x + states_t.vx * self.dt
        z = states_t.z + states_t.vz * self.dt
        y = states_t.y + states_t.vy * self.dt
        vx = states_t.vx + self.choosemode(states_t, self.dt)[0]
        vz = states_t.vz + self.choosemode(states_t, self.dt)[1]
        vy = states_t.vy + self.choosemode(states_t, self.dt)[2]
        ball = sphere(bomb=sphere(pos=vector(x,y,z),radius=0.075,color=color.white))
        ball.velocity = vector(vx,vy,vz)
        #---------
        self.states.append(states(ball, states.t+self.dt))
        
class choosemode:
    global [a1,a2,vd,delta,] = factor[:]
    global B2/m = a1 + a2/(1+math.exp((v-vd)/delta))

    def Normalball(self, states_t, d_t):
        d_vx = - B2/m * states_t.v * states_t.vx * d_t
        d_vz = - B2/m * states_t.v * states_t.vz * d_t
        d_vy = - g *dt - B2/m * states_t.v * states_t.vy * d_t
        d_v = [d_vx,d_vz,d_vy]
        return d_v

    def Spinball(self, states_t, d_t):
        d_vx = - B2/m * states_t.v * states_t.vx * d_t
        d_vz = - S0/m * states_t.vx * w * d_t
        d_vy = -g * d_t
        d_v = [d_vx,d_vz,d_vy]
        return d_v

    def knuckleball(self, states_t, dt):

        #---------
