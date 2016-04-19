import math
import easygui
from visual import *

def readfile():
    infile = open('parameter.txt', 'r')
    linelist = infile.readlines()
    print linelist[0]
    factor = []
    for char in linelist[1].split():
        factor.append(float(char))
    return factor

factor = readfile()
print factor

class States:
    global g,l,q,Omega,FD
    [g,l,q,Omega,FD]=factor[:]

# ini_state=[omega, theta, t]
    def __init__(self, ini_state=[0,0], t=0):
        self.omega = ini_state[0]
        self.theta = ini_state[-1]
        self.t = t
#        self.x = ball.pos.x
#        self.z = ball.pos.z
#        self.y = ball.pos.y
#        self.vx = ball.velocity.x
#        self.vz = ball.velocity.z
#        self.vy = ball.velocity.y
#        self.v = mag(ball.velocity)

class Pendulum:
        
    def __init__(self, _sta = States(), d_t=0.01):
        self.states = []
        self.states.append(_sta)
        self.dt = d_t
        self.keys = self.choosemode()
        self.modes = Choosemode()
        
    def Next(self):
        [key_0,key_1,key_2] = self.keys
        states_t = self.states[-1]
        
        add = [0]
        if key_0 == 'Simple': 
            add = add + self.modes.Simple(states_t, self.dt)
        else:
            add = add + self.modes.Not_Simple(states_t, self.dt)
        if key_1 == 'Drag': 
            add = add + self.modes.Drag(states_t, self.dt)
        if key_2 == 'ForceD': 
            add = add + self.modes.ForceD(states_t, self.dt)
        omega = states_t.omega + add[0]
        theta = states_t.theta + omega * self.dt
        t = states_t.t + self.dt

        self.states.append(States([omega,theta], t))
        return [omega, theta, t]
#        ball = sphere(pos=vector(x,y,z),radius=0.075,color=color.white)
#        ball.velocity = vector(vx,vy,vz)

    def choosemode(self):
        key_0 = easygui.buttonbox('Choose the small angle approximation or not','CHOOSE',['Simple', 'Not_Simple'])
        key_1 = easygui.buttonbox('Choose whether to add the damping force or not','CHOOSE',['Drag','Skip!'])
        key_2 = easygui.buttonbox('Choose whether to add the driving force or not','CHOOSE',['ForceD','Skip!'])
        return [key_0,key_1,key_2]

    def path(self):
        states_t = self.states[-1]
        pass
#        [x,y,z] = [states_t.x,states_t.y,states_t.z]
#        return sphere(pos=vector(x,y,z), radius=0.04, color=color.white)
        

class Choosemode:
    global g,l,q,omega_D,FD
    [g,l,q,omega_D,FD]=factor[:]
    def __init__(self):
        pp = 'pinkie pie'

    def Simple(self, states_t, dt):
        d_omega = - g/l * states_t.theta * dt
        return [d_omega]

    def Drag(self, states_t, dt):
        d_omega = - q * states_t.omega * dt
        return [d_omega]

    def ForceD(self, states_t, dt):
        d_omega = FD * math.sin(omega_D * states_t.t) * dt
        return [d_omega]

    def Not_Simple(self, states_t, dt):
        d_omega = - g/l * math.sin(states_t.theta) * dt
        return [d_omega]

# ----------
def release():
    debugger = 0
    ini_theta = int(easygui.integerbox('Make ini_theta to be')) # degree
    ini_state = [0, ini_theta] 
    temp = States(ini_state)
    pendulum_t = Pendulum(temp, 0.01)
    counter = 0
    while True:
        rate(100)
        counter += 1
        if counter>=1000:
            debugger += 1
            print debugger
            break
        pendulum_t.Next()
    return pendulum_t

release()
