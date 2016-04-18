import math
import easygui
import sys
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
    global g,a1,a2,vd,delta,S0_m,mph,rpm
    [g,a1,a2,vd,delta,S0_m,mph,rpm]=factor[:]

    def __init__(self, ball= sphere(pos=(0,0,0),velocity=vector(0,0,0),radius=0.01,color=color.black), t=0):
        self.x = ball.pos.x
        self.z = ball.pos.z
        self.y = ball.pos.y
        self.vx = ball.velocity.x
        self.vz = ball.velocity.z
        self.vy = ball.velocity.y
        self.t = t
        self.v = mag(ball.velocity)

class Baseball:
        
    def __init__(self, _sta = States(), d_t=0.01):
        self.key = self.choose()
        self.states = []
        self.states.append(_sta)
        self.dt = d_t
        self.choosemode = Choosemode()
        
    def Next(self):
        key = self.key
        states_t = self.states[-1]
        x = states_t.x + states_t.vx * self.dt
        z = states_t.z + states_t.vz * self.dt
        y = states_t.y + states_t.vy * self.dt

        if key == 'Normal': 
            [vx,vz,vy] = self.choosemode.Normalball(states_t, self.dt)
        elif key == 'Spin': 
            [vx,vz,vy] = self.choosemode.Spinball(states_t, self.dt)
        elif key == 'Knuckle': 
            [vx,vz,vy] = self.choosemode.Knuckleball(states_t, self.dt)
        elif key == 'Exit': sys.exit(0)

        ball = sphere(pos=vector(x,y,z),radius=0.075,color=color.white)
        ball.velocity = vector(vx,vy,vz)
        #---------
        self.states.append(States(ball, states_t.t+self.dt))
        return self.path()

    def choose(self):
        key = easygui.buttonbox('Normal/Spin/Knuckle Ball','CHOOSEMODE',['Normal','Spin','Knuckle','Exit'])
        return key

    def path(self):
        states_t = self.states[-1]
        [x,y,z] = [states_t.x,states_t.y,states_t.z]
        return sphere(pos=vector(x,y,z), radius=0.04, color=color.white)
        

class Choosemode:
    global g,a1,a2,vd,delta,S0_m,mph,rpm,w,w_k
    [g,a1,a2,vd,delta,S0_m,mph,rpm] = factor[:]
    w = 2000*rpm
    w_k = 12*rpm
    def __init__(self,sita=1.6):
        self.spin = []
        self.spin.append(sita)

    def Normalball(self, states_t, dt):
        B2_m = a1 + a2/(1+math.exp((states_t.v-vd)/delta))
        d_vx = - B2_m * states_t.v * states_t.vx * dt
        d_vz = - B2_m * states_t.v * states_t.vz * dt
        d_vy = - g * dt - B2_m * states_t.v * states_t.vy * dt
        vx = states_t.vx + d_vx 
        vz = states_t.vz + d_vz
        vy = states_t.vy + d_vy
        v = [vx,vz,vy]
        return v

    def Spinball(self, states_t, dt):
        B2_m = a1 + a2/(1+math.exp((states_t.v-vd)/delta))
        d_vx = - B2_m * states_t.v * states_t.vx * dt
        d_vz = - S0_m * states_t.vx * w * dt
        d_vy = -g * dt
        vx = states_t.vx + d_vx
        vz = states_t.vz + d_vz
        vy = states_t.vy + d_vy
        v = [vx,vz,vy]
        return v

    def Knuckleball(self, states_t, dt):
        B2_m = a1 + a2/(1+math.exp((states_t.v-vd)/delta))
        sita = self.spin[-1]
        d_vx = - B2_m * states_t.v * states_t.vx * dt
        d_vz = - B2_m * states_t.v * states_t.vz * dt - S0_m * states_t.vx * w_k * dt + g * 0.5 * (math.sin(4*sita)-0.25*math.sin(8*sita)+0.08*math.sin(12*sita)-0.025*math.sin(16*sita)) * dt
        d_vy = -g * dt
        vx = states_t.vx + d_vx
        vz = states_t.vz + d_vz
        vy = states_t.vy + d_vy
        v = [vx,vz,vy]
        sita = self.spin[-1] + (w_k) * dt
        self.spin.append(sita)
        print d_vz
        return v

# ----------
def hit(baseball,home_plate):
    debugger = 0
    angle = int(easygui.integerbox('Initial velocity is 45m/s\nChoose Pitching Angle')) # degree
    init_v = 45 # m/s 
    init_vx = init_v * math.cos(math.radians(angle))
    init_vy = init_v * math.sin(math.radians(angle))
    init_vz = 0
    baseball.velocity = vector(init_vx,init_vy,init_vz)
    temp = States(baseball)
    Baseball_t = Baseball(temp, 0.01)
    while True:
        rate(100)
        if Baseball_t.states[-1].y < 0 or Baseball_t.states[-1].x > home_plate.x:
            debugger += 1
            print debugger
            easygui.msgbox('Horizenal_diffraction(m): '+str(Baseball_t.states[-1].z)+'\nHeight(m): '+str(Baseball_t.states[-1].y))
            break
        Baseball_t.Next()
    return Baseball_t

earth = box(pos=vector(0,0,0),size=(40,0.01,40),color=color.blue)
baseball = sphere(pos=vector(0,1.65,0),radius=0.075,color=color.red)
home_plate = box(pos=vector(18.288,0,0),length=0.01,height=0.05,width=10,color=color.red)
axis_y = arrow(pos=(0,0,0), axis=(0,5,0), shaftwidth=0.01, color=color.black)
axis_z = arrow(pos=(0,0,0), axis=(0,0,5), shaftwidth=0.01, color=color.black)
axis_x = arrow(pos=(0,0,0), axis=(5,0,0), shaftwidth=0.01, color=color.black)


hit(baseball,home_plate)

        #---------
