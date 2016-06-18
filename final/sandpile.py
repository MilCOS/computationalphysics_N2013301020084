import numpy as np
from matplotlib import cm
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
#    Z1[i-1,j] -= 1
#    Z1[i,j-1] -= 1

def evolve(rc):
    global Z1,pinkie
    pinkie = np.zeros([L,L])
    counter = 0
    while (np.sum(np.where(Z1>rc)) > 0):
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
                    pinkie[i,j] += 1
                else: pass
        Z1 = boundary_con(Z1)
    return counter

def draw(Z_temp):
    fig, ax = plt.subplots()
    cax = ax.imshow(Z_temp, interpolation='nearest', cmap=cm.coolwarm)
    ax.set_title('Sandpile with vertical colorbar')
    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    cbar = fig.colorbar(cax, ticks=[0, 4, 1], drawedges=True)
    cbar.ax.set_yticklabels(['0', '1', '2', '3'])  # vertically oriented colorbar
    plt.show()
    


L = 50 #size of the sandpile
rc = 3 # Give the threshold value
N = 200

xs = np.arange(0,L,1)
ys = np.arange(0,L,1)
x,y = np.meshgrid(xs,ys)

pinkie = np.zeros([L,L])
twili = np.ones([L,L])
Z1 = np.random.random_integers(rc-1,rc+1,size=[L,L])
note1,note2 = 0,0
for k in range(7000):
    pickadd()
note1 = evolve(rc)
note2 += note1
draw(Z1)
D = []
for k in range(N):
    pickadd()
    note1 = evolve(rc)
    note2 += note1
    #print(note1, note2)
    D.append(note1)
    pinkie[np.where(pinkie>0)] = 1
    twili += pinkie 
draw(twili)
print(float(N)/sum(D))
