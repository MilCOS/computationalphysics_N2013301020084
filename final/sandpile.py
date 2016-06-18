import numpy as np
from matplotlib import pyplot as plt

def boundary_con(Z_temp):
    Z_temp[:,0],Z_temp[:,L-1] = 0,0
    Z_temp[0,:],Z_temp[L-1,:] = 0,0
    return Z_temp

def pickadd():
    global Z1
    i,j = L * np.random.uniform(0,1,size=2)
    i,j = int(i),int(j)
    Z1[i,j] += 1
    Z1[i-1,j] -= 1
    Z1[i,j-1] -= 1

def evolve(rc):
    global Z1,pinkie
    pinkie = np.zeros([L,L])
    counter = 0
    pickadd()
    while (np.sum(np.where(Z1>rc)) > 0):
        Z1 = boundary_con(Z1)
        for i in range(1,L-1):
            for j in range(1,L-1):
    #            Z1[i,j] += 2
    #            Z1[i-1,j] -= 1
    #            Z1[i,j-1] -= 1
                if (Z1[i,j]>rc):
                    counter += 1
                    Z1[i,j]   -= 4
                    Z1[i,j+1] += 1
                    Z1[i+1,j] += 1
                    Z1[i-1,j] += 1
                    Z1[i,j-1] += 1
    #                twili[i,j] -= 1
                    pinkie[i,j] += 1
                else: pass
    return counter

L = 100 #size of the sandpile
rc = 3 # Give the threshold value

xs = np.arange(0,L,1)
ys = np.arange(0,L,1)
x,y = np.meshgrid(xs,ys)

pinkie = np.zeros([L,L])
twili = np.ones([L,L])
Z1 = twili*int(rc*np.random.uniform(0,2))
note = 0

for k in range(10):
    note += evolve(rc)

#plt.scatter(x, y, Z1)
plt.scatter(x, y, pinkie)
print(note)
plt.show()
