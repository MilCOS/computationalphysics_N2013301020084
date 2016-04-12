from matplotlib.pyplot import *
import math
import python-visual
import easygui

class flight_state:
    def __init__(self, ball, _t = 0):
        self.x = ball.pos.x
        self.y = ball.pos.y
        self.vx = ball.velocity.x
        self.vy = ball.velocity.y
        self.t = _t

class baseball:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.ball_flight_state = []
        self.ball_flight_state.append(_fs)
        self.dt = _dt

    def next_state(self, current_state):
        global g
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

    def shoot(self):
        while not(self.ball_flight_state[-1].y < 0):
            self.ball_flight_state.append(self.next_state(self.ball_flight_state[-1]))
        self.ball_flight_state[-1].y = 0
        return  [self.ball_flight_state[-1].x, self.ball_flight_state[-1].y] # final position

    def show_trajectory(self,v = 340,angle = 45):
        #show()

class wind_drag(ball):
    def next_state(self, current_state):
        global g, b2m
        v = math.sqrt(current_state.x * current_state.x + current_state.y * current_state.y)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - b2m * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

class spin(ball):
    def next_state(self, current_state):
        global g, b2m
        v = math.sqrt(current_state.x * current_state.x + current_state.y * current_state.y)
        next_x = current_state.x + current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        Delta = (1 - a * current_state.y / T_0)**Alpha
        next_vx = current_state.vx - Delta * b2m * v * current_state.vx * self.dt
        next_vy = current_state.vy - g * self.dt - Delta * b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)
class knuckleball(ball):
    def next_state(self, current_state):


def ini(v = 340, angle = 45): # The sonic bomb
    vx = v * math.cos(math.radians(angle))
    vy = v * math.sin(math.radians(angle))
    ini = flight_state(0, 0, vx, vy, 0)
    return ini


def mode1():
    v = 340
    for angle in range(25,85,5):
        i += 1
        temp = cannon(ini(v, angle), _dt = 0.1)
        A.append(temp)
    for i in range(0,12,1):
        angle = 25 + 5*i
        A[i].shoot()
        A[i].show_trajectory(v, angle)
    show()
    choosemode()
def mode2(): #air resistance
    B = []
    i = 0
    angle = 45
    k = easygui.integerbox("Input the number of curved lines(1~)")
    if k == None: choosemode()
    for v in range(100,(k+5)*20,20):
        i += 1
        temp = drag_cannon(ini(v, angle), _dt = 0.1)
        B.append(temp)
    choice = easygui.buttonbox('Choose path or velocity to polt','Choice',['trajectory','velocity change'])
    if choice == 'trajectory':
        for i in range(0,k-1,1):
            v = 100 + 20*i
            B[i].shoot()
            B[i].show_trajectory(v,angle)
        show()
    if choice == 'velocity change':
        for i in range(0,k-1,1):
            v = 100 + 20*i
            B[i].shoot_v()
            B[i].show_velocity(v,angle)
        show()
    choosemode()
def mode3(): # density change
    target_x = int(easygui.enterbox('Input the target position','Initialise the question')) #m
    limit_d = float(easygui.enterbox('Allowable errors about the distance between target and landing point','CHOOSE ERROR')) #m
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
                c.show_trajectory(v, angle)
                show()
                out = 'Final Landing Point: '+str(out)
                easygui.msgbox(out, 'Target Position: '+str(target_x))
                break
    choosemode()
def choosemode():
    out = easygui.buttonbox('No Air | Air Resistance | Density Change | Quit','CHOOSE MODE',[1,2,3,'Quit'])
    if out == 'Quit': print 'Hello World'
    elif int(out) == 1: mode1()
    elif int(out) == 2: mode2()
    elif int(out) == 3: mode3()
choosemode()
# b = drag_cannon(flight_state(0, 0, 100, 50, 0), _dt = 0.1)
# b.shoot()
