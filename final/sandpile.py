import numpy as np
import data_analyse as da
from matplotlib import cm
from matplotlib import pyplot as plt

def boundary_con(Z_temp,l1=0,l2=1): #l1=45,l2=55 et.cl.
    Z_temp[:,0],Z_temp[:,L-1] = 0,0
    Z_temp[0,:],Z_temp[L-1,:] = 0,0
    Z_temp[l1:l2,l1],Z_temp[l1:l2,l2]=0,0
    Z_temp[l1,l1:l2],Z_temp[l2,l1:l2]=0,0
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
        Z1 = boundary_con(Z1,l1=45,l2=55)
    return counter

def draw(Z_temp):
    fig, ax = plt.subplots()
    cax = ax.imshow(Z_temp, interpolation='nearest', cmap=cm.coolwarm)
    ax.set_title('Sandpile with vertical colorbar')
    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    cbar = fig.colorbar(cax, ticks=[0, np.ma.max(Z_temp), 1], drawedges=True)
    #cbar.ax.set_yticklabels(['0', str(np.ma.max(Z_temp))])  # vertically oriented colorbar
    plt.show()

#def residuals(p, y, x):
#    tau = p
#    return math.log10(y) - tau*(math.log10(x))
#def myfit(x, y):
#    p0 = -1.0
#    plsq = optimize.leastsq(residuals, p0, args=(y, x))
#    return plsq
    
def readfile():
    data = []
    infile = open("data.txt", "r")
    aline = infile.readline()
    while aline:
        items = aline.split()
        data.append(int(items[0])+1)
        aline = infile.readline()
    infile.close()
    return np.array(data)
def writefile(aline):
    outfile = open("data.txt", "w")
    for k in range(len(aline)):
        items = aline[k]
        outfile.write(str(items) + '\n')
    outfile.close()
def plotD(array1,array2):
    fig, ax_l = plt.subplots()
    ax_l.set_xscale("log")
    ax_l.set_yscale("log")
    ax_l.scatter(array1,array2)
    ax_l.set_xlim(1e0, 1e4)
    ax_l.set_ylim(1e-4, 1e0)
    ax_l.set_title('Distribution of avalanche sizes')
    ax_l.set_ylabel('number of avalanches')

    fit = da.myfit(array1[:9],array2[:9])
    x = np.arange(1e0,1e1)
    ax_l.plot(x, da.func(x, fit[0]), label=u'$\tau='+str(fit[0])+'$')
    fit = da.myfit(array1[9:18],array2[9:18])
    x = np.arange(1e1,1e2)
    ax_l.plot(x, da.func(x, fit[0]), label=u'$\tau='+str(fit[0])+'$')
    fit = da.myfit(array1[18:27],array2[18:27])
    x = np.arange(1e2,1e3)
    ax_l.plot(x, da.func(x, fit[0]), label=u'$\tau='+str(fit[0])+'$')
    fit = da.myfit(array1[27:],array2[27:])
    x = np.arange(1e3,1e4)
    ax_l.plot(x, da.func(x, fit[0]), label=u'$\tau='+str(fit[0])+'$')
    fit = da.myfit(array1,array2)
    x = np.arange(1e0,1e4)
    ax_l.plot(x, da.func(x, fit[0]), label=u'$\tau='+str(fit[0])+'$')
    ax_l.legend()
    plt.show()

def count_in_unit():
    data_y = readfile() # values have been increased by 1 when readfile
    s,f = [],[]
    l = 9 # Do not change this value
    for i in range(int(np.log10(len(data_y)))):
        print(i)
        delta = float(10**(i+1)-10**i)/l
        for k in range(l):
            tempindex = np.where(((10**i+k*delta)<=data_y) & (data_y<(10**i+(k+1)*delta)))
            temparray = data_y[tempindex]
            n = len(temparray)
            print(n)
            f.append(float(n)/float(len(data_y)))
            s.append(10**i+k*delta) 
    plotD(s,f) # plot needs arrays
    f,s = np.array(f),np.array(s)
    f = f[np.where(f>0)]
    s = s[np.where(f>0)]
def count_in_average():
    data_y = readfile() # values have been increased by 1 when readfile
    s,f = [],[]
    l = 9 # Do not change this value
    for i in range(int(len(data_y))):
        tempindex = np.where((i+1<=data_y)&(data_y<i+2))
        temparray = data_y[tempindex]
        n = len(temparray)
        f.append((float(n))/float(len(data_y)))
        s.append(i+1)
    f,s = np.array(f),np.array(s)
    f = f[np.where(f>0)]
    s = s[np.where(f>0)]
    z1 = np.polyfit(np.log(s),np.log(f),1)
    fit = np.poly1d(z1)
    fig, ax = plt.subplots()
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e0, 1e4)
    ax.set_ylim(1e-4, 1e0)
    ax.set_title('Distribution of sizes')
    ax.set_ylabel('number of avalanches')
    ax.scatter(s,f,c='black',marker='.')
    ax.plot(s, np.exp(fit(np.log(s))), linestyle='--', label=str(fit))
    plt.legend()
    plt.show()

# main_program
L = 100 #100   size of the sandpile
rc = 3 #3     Give the threshold value
N = 400 #10000 the time you'd like to trigger an avalanche

xs = np.arange(0,L,1)
ys = np.arange(0,L,1)
x,y = np.meshgrid(xs,ys)

pinkie = np.zeros([L,L])
twili = np.zeros([L,L])
Z1 = np.random.random_integers(rc-1,rc+1,size=[L,L])
note1,note2 = 0,[]
for k in range(1000):#number: randomly add the sand(maybe save for another question))
    pickadd()
note1 = evolve(rc)
note2.append(note1)
draw(Z1)
D = []
for k in range(N):
    pickadd()
    note1 = evolve(rc)
    note2.append(note1)
    #print(note1, sum(note2))
    D.append(note1)
    pinkie[np.where(pinkie>0)] = 1
    twili += pinkie 
print(note1,sum(note2),sum(D))
print(float(N)/sum(D))
draw(twili)
#writefile(D)
#count_in_unit()
#count_in_average()
