from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import numpy as np
datafile_1 = open("gauss_seidel.txt", "r")
datafile_2 = open("sor_method.txt", "r")
x = []
y = []
v = []
# be aware no L!
i = 0
# chang the index
for aline in datafile_1: 
    values = aline.split()
    for j in range(len(values)):
        temp = float(values[j])
        v.append(temp*10)
        y.append(j)
        x.append(i)
    i +=1
print len(x),len(y),len(v)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,v,c='r',marker='.')
plt.show()

L_gauss = [16,18,20,22,24,26,28,30,36,40,46,50]
N_gauss = [76,94,116,143,58,76,95,117,190,247,342,414]
L_gauss_a = [24,26,28,30,36,40,46,50]
N_gauss_a = [58,76,95,117,190,247,342,414]
L_sor =   [16,20,26,28,30,32,36,40,44,46,48,50]
N_sor = [27,42,55,52,56,58,59,71,92,64,98,102]
L_sor_a =   [16,20,26,28,30,32,36,40,44,48,50]
N_sor_a = [27,42,55,52,56,58,59,71,92,98,102]
print len(L_gauss),len(N_gauss),len(L_sor),len(N_sor)
ax1=plt.subplot(221)  
plt.xlabel('$L$')
plt.ylabel('$N_{iter}$')
ax2=plt.subplot(222)  
plt.xlabel('$L$')
plt.ylabel('$N_{iter}$')
ax3=plt.subplot(223)  
plt.xlabel('$L$')
plt.ylabel('$N_{iter}$')
ax4=plt.subplot(224)  
plt.xlabel('$L$')
plt.ylabel('$N_{iter}$')
ax1.scatter(L_gauss,N_gauss,c='b')
ax2.scatter(L_sor,N_sor,c='g')

N_gauss_aa = [math.sqrt(N_gauss_a[i]) for i in range(len(N_gauss_a))]
z1 = np.polyfit(L_gauss_a,N_gauss_aa,1)
fit_gauss = (np.poly1d(z1))**2
ax3.scatter(L_gauss_a,N_gauss_a,c='g')
#ax3.scatter(c='r',marker='v')
x = np.arange(13,52)
ax3.plot(x, fit_gauss(x), linestyle='--')

z2 = np.polyfit(L_sor,N_sor,1)
fit_sor = np.poly1d(z2)
ax4.scatter(L_sor_a,N_sor_a,c='g')
ax4.scatter(46,64,c='r',marker='v')
x = np.arange(13,52)
ax4.plot(x, fit_sor(x), linestyle='--', label="N=1.862L + 0.1051")

plt.show()
print fit_gauss,fit_sor
