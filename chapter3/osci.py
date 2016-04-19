import math
import easygui
from visual import *
import matplotlib.pyplot as pl

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
        
    def __init__(self, _sta = States(), d_t=0.01, para=[1.0,2.0,0.2]):
        self.states = []
        self.states.append(_sta)
        self.dt = d_t
        self.keys = self.choosemode()
        self.modes = Choosemode(para)
        
    def Next(self):
        [key_0,key_1,key_2] = self.keys
        states_t = self.states[-1]
        
        add = 0
        if key_0 == 'Simple': 
            add = add + self.modes.Simple(states_t, self.dt)
        if key_0 == 'Not_Simple':
            add = add + self.modes.Not_Simple(states_t, self.dt)
            print 'pinkie pie'
        if key_1 == 'Drag': 
            add = add + self.modes.Drag(states_t, self.dt)
            print 'rainbowdash',add
        if key_2 == 'ForceD': 
            add = add + self.modes.ForceD(states_t, self.dt)
        omega = states_t.omega + add
        theta = states_t.theta + omega * self.dt
        t = states_t.t + self.dt

        if (theta <= - math.pi):    theta = theta + math.pi
        if (theta > math.pi):    theta = theta - math.pi
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
    global g,l
    [g,l]=factor[:2]

    def __init__(self, para=[1.0,2.0,0.2]):
        pp = 'pinkie pie'
        self.q = para[0]
        self.omega_D = para[1]
        self.FD = para[-1]

    def Simple(self, states_t, dt):
        d_omega = - g/l * states_t.theta * dt
        return d_omega

    def Drag(self, states_t, dt):
        d_omega = - self.q * states_t.omega * dt
        return d_omega

    def ForceD(self, states_t, dt):
        d_omega = self.FD * math.sin(self.omega_D * states_t.t) * dt
        return d_omega

    def Not_Simple(self, states_t, dt):
        d_omega = - g/l * math.sin(states_t.theta) * dt
        return d_omega

# ----------
def release(ini_theta = 10, q=1.0, omega_D=2.0, FD=0.2):
    para = [q, omega_D, FD] # 'package' the parameters

    debugger = 0
    theta = []
    t = []

    ini_state = [0, ini_theta] 
    print(ini_theta)

    temp = States(ini_state)
    pendulum_t = Pendulum(temp, 0.01, para)
    counter = 0
    while True:
        rate(2000)
        counter += 1
        if counter >= 1000: #The real time is 10 second now
            debugger += 1
            print debugger
            break
        result = pendulum_t.Next()
        theta.append(result[1])
        t.append(result[-1])
    # waiting for regular plot Ha?
    ax = pl.axes(xlim=(0, 10), ylim=(-0.4, 0.4))
    pl.plot(t, theta, label="omega_D="+str(para[0])) #choose i in para[i] to match your changing` parameter
    pl.legend(loc='lower right')

def draw(q=1.0, omega_D=2.0, FD=0.2):
    ini_theta = math.radians(float(easygui.enterbox('Make ini_theta to be in degree'))) # degree shouldn't be zero or the pendulum will keep still
    fig = pl.figure(figsize=(19,12))
    pl.title("Oscillator")
    pl.xlabel(r'$time(s)$', fontsize=20)
    pl.ylabel(r'$\theta(radians)$', fontsize=20)

    for i in range(len(omega_D)):
        release(ini_theta, q[i], omega_D[0], FD[0])
        print omega_D[i]
        pl.savefig("Pendulum_"+str(i)+".png",dpi=72)

q = [0, 1.0, 2.0]
omega_D = [3.0,2.0,1.0]
FD = [0.2, 0.5, 1.0]


draw(q, omega_D, FD)
pl.show()
