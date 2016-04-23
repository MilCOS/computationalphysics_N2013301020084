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
        if key_0 == 'NotSimple':
            add = add + self.modes.NotSimple(states_t, self.dt)
        if key_1 == 'Drag': 
            add = add + self.modes.Drag(states_t, self.dt)
        if key_2 == 'ForceD': 
            add = add + self.modes.ForceD(states_t, self.dt)
        omega = states_t.omega + add
        theta = states_t.theta + omega * self.dt
        t = states_t.t + self.dt

        if (theta <= - math.pi):    theta = theta + 2*math.pi
        if (theta > math.pi):    theta = theta - 2*math.pi
        self.states.append(States([omega,theta], t))
        keys = '+'.join(self.keys)
        return [keys, omega, theta, t]
#        ball = sphere(pos=vector(x,y,z),radius=0.075,color=color.white)
#        ball.velocity = vector(vx,vy,vz)

    def choosemode(self):
        key_0 = easygui.buttonbox('Choose the small angle approximation or not','CHOOSE',['Simple', 'NotSimple'])
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

    def NotSimple(self, states_t, dt):
        d_omega = - g/l * math.sin(states_t.theta) * dt
        return d_omega

# ----------

def regular_text(q=1.0, omega_D=2.0, FD=0.2):
    if len(q) != 1: 
        pl.text(1, 0.3, r'$\Omega_D = '+str(omega_D)+ '$ \n' + r'$F_D='+str(FD)+'$', color='black', fontsize=20)
    if len(omega_D) != 1:
        pl.text(1, 0.3, r'$q = '+str(q)+ '$ \n' + r'$F_D='+str(FD)+'$', color='black', fontsize=20)
    if len(FD) != 1:
        pl.text(1, 0.3, r'$q = '+str(q)+ '$ \n' + r'$\Omega_D='+str(omega_D)+'$', color='black', fontsize=20)
    pl.xlabel(r'$\t$', fontsize=20)
    pl.ylabel(r'$\theta$', fontsize=20)

def release(ini_theta = 10, q=0, omega_D=0, FD=0, d_t=0.01):
    para = [q, omega_D, FD] # 'package' the parameters

    debugger = 0
    omega = [0]
    theta = [ini_theta]
    t = [0]

    ini_state = [0, ini_theta] 
    print(ini_theta)

    temp = States(ini_state)
    pendulum_t = Pendulum(temp, d_t, para)
    counter = 0
    while True:
        
        if counter >= 150000: #The real time is 40 second now
            debugger += 1
            print debugger
            break
        result = pendulum_t.Next()
        if ((counter)%300 == 0): #Attractor controler
            theta.append(result[2])
            omega.append(result[1])
            t.append(result[-1])
        counter += 1

    ax = pl.axes(xlim=(-4, 4), ylim=(min(omega)-0.2, max(omega)+0.2))
    pl.scatter(theta, omega, linestyle=':', color='Black', label="Omega_D="+str(para[1])) #choose i in para[i] to match your changing` parameter
    pl.legend(loc='lower right')
    return result[0]

def draw_D(q=0, omega_D=0, FD=0):
    ini_theta = (float(easygui.enterbox('Make ini_theta to be in radians'))) # degree shouldn't be zero or the pendulum will keep still
    fig = pl.figure(figsize=(19,12))

    for i in range(len(omega_D)):                    # Be aware about the index
        keys = release(ini_theta, q[0], omega_D[i], FD[0], 0.01*math.pi)  # 
        regular_text(q[:1],omega_D[:],FD[:1])               #
        pl.title(keys+" Oscillator "+'$\Theta = '+str(math.degrees(ini_theta))+'^o$')
        pl.savefig("omega_D_attractor_"+str(i)+".png",dpi=72) #

q = [0.5]
omega_D = [2./3.,2./3.-0.001,2./3.+0.001]
FD = [1.2,1.1]


draw_D(q, omega_D, FD)
pl.show()
