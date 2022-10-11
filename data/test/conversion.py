import numpy as np
from utils import *

curve=np.loadtxt('wave_pts_final.txt')
###normalize + negate
curve[:,3:]=-curve[:,3:]/np.tile(np.linalg.norm(curve[:,3:],axis=1),(3,1)).T


np.savetxt('Curve_dense.csv', curve, delimiter=',')