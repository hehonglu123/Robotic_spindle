import numpy as np
import sys	
sys.path.append('../../toolbox')
from utils import *

curve=np.loadtxt('wave_pts_final.txt')
###normalize + negate
curve[:,3:]=-curve[:,3:]/np.tile(np.linalg.norm(curve[:,3:],axis=1),(3,1)).T

###force normal down
curve[:,3:]=np.zeros(curve[:,3:].shape)
curve[:,-1]=-1

curve[:,0]=moving_average(curve[:,0],n=11,padding=True)
curve[:,1]=moving_average(curve[:,1],n=11,padding=True)
curve[:,2]=moving_average(curve[:,2],n=11,padding=True)


np.savetxt('Curve_dense.csv', curve, delimiter=',')