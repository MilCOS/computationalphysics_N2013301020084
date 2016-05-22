import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
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
    print len(values)
    for j in range(len(values)):
        temp = float(values[j])
        v.append(temp*10)
        y.append(j)
        x.append(i)
    i +=1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,v,c='r',marker='.')
plt.show()

