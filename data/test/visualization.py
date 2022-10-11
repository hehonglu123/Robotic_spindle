import numpy as np
from utils import *

curve=np.loadtxt('wave_pts_final.txt')

plt.plot(curve[:,0],label='x')
plt.plot(curve[:,1],label='y')
plt.plot(curve[:,2],label='z')
plt.legend()
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot3D(curve[::10,0],curve[::10,1],curve[::10,2], 'gray')
# ax.scatter(curve[:,0], curve[:,1],curve[:,2], 'gray')
ax.quiver(curve[::10,0],curve[::10,1],curve[::10,2],1*curve[::10,3],1*curve[::10,4],1*curve[::10,5])
ax.set_xlabel('x (mm)')
ax.set_ylabel('y (mm)')
ax.set_zlabel('z (mm)')
plt.show()