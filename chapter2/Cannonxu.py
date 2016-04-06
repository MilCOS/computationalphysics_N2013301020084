from matplotlib.pyplot import *
import math
import easygui

g = 9.8 #m/s**2
b2m = 1e-5 
a = 0.0065 # K/m
T_0 = 300 # K
Alpha = 2.5

class flight_state:
    def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.vx = _vx
        self.vy = _vy
        self.t = _t

class cannon:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.cannon_flight_state = []
        self.cannon_flight_state.append(_fs)
        self.dt = _dt
        # self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy

    def next_state(self, current_state):
        global g
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

    def shoot(self):
        while not(self.cannon_flight_state[-1].y < 0):
            self.cannon_flight_state.append(self.next_state(self.cannon_flight_state[-1]))
        r = - self.cannon_flight_state[-2].y / self.cannon_flight_state[-1].y
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = 0
        return  [self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y] # final position

    def show_velocity(self):
        t = []
        v = []
        for fs in self.cannon_flight_state:
            vx.append(flight_state.t)
            vi = math.sqrt((flight_state.vx)**2 + (flight_state.vy)**2)
            vy.append(vi)

        plot(vx,vy)
        #show()

    def show_trajectory(self):
        x = []
        y = []
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)
        plot(x,y)
        ylabel('y_distance /m')
        xlabel('x_distance /m')
        title('Trajectory of cannon')
        #show()

class drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m
        v = sqrt(current_state.x * current_state.x + current_state.y * current_state.y)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - b2m * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

class dense_air(cannon):
    def next_state(self, current_state):
        global g, b2m
        v = sqrt(current_state.x * current_state.x + current_state.y * current_state.y)
        next_x = current_state.x + current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        Delta = (1 - a * current_state.y / T_0)**Alpha
        next_vx = current_state.vx - Delta * b2m * v * current_state.vx * self.dt
        next_vy = current_state.vy - g * self.dt - Delta * b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

def ini(v = 340, angle = 45): # The sonic bomb
    vx = v * math.cos(math.radians(angle))
    vy = v * math.sin(math.radians(angle))
    ini = flight_state(0, 0, vx, vy, 0)
    return ini

target_x = int(easygui.enterbox('Input the target position','Initialise the question')) #m
limit_d = float(easygui.enterbox('Allowable errors about the distance between target and landing point','CHOOSE ERROR')) #m

def mode1():
    A = []
    i = 0
    angle = 45
    for v in range(100,340,40):
        i += 1
        temp = cannon(ini(v, angle), _dt = 0.1)
        A.append(temp)
    for i in range(0,6,1):
        A[i].shoot()
        A[i].show_trajectory()
    show()
def mode2(): #air resistance
    B = []
    i = 0
    v = 340
    k = easygui.integerbox("Input the drawing number(0~12)")
    if k == None: choosemode()
    for angle in range(30,(k+6)*5,5):
        i += 1
        temp = drag_cannon(ini(v, angle), _dt = 0.1)
        B.append(temp)
    for i in range(0,k,1):
        B[i].shoot()
        B[i].show_trajectory()
    show()
def mode3(): # density change
    d = target_x
    limit = limit_d
    while d > limit:
        c = dense_air(ini(), _dt = 0.1)
        d = abs(c.shoot()[0] - target_x)
        if d < limit: break
        final = []
        for angle in range(5,90,5):
            final.append(c.shoot()[0])
        i = final.index(max(final))
        angle = range(5,90,5)[i]
        for v in range(100,target_x,1):
            c = dense_air(ini(v, angle), _dt = 0.1)
            d = abs(c.shoot()[0] - target_x)
            if d < limit: 
                c = dense_air(ini(v, angle), _dt = 0.1)
                out = c.shoot()
                c.show_trajectory()
                show()
                out = 'Final Landing Point: '+str(out)
                easygui.msgbox(out, 'Target Position: '+str(target_x))
                break
def choosemode():
    out = easygui.buttonbox('No Air | Air Resistance | Density Change','CHOOSE MODE','123')
    if int(out) == 1: mode1()
    elif int(out) == 2: mode2()
    elif int(out) == 3: mode3()
    else: print 'debugger'
choosemode()
# b = drag_cannon(flight_state(0, 0, 100, 50, 0), _dt = 0.1)
# b.shoot()
