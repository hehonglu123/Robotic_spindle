import numpy as np
import sys
sys.path.append('../../toolbox')
from utils import *
from pandas import *

curve_js = read_csv('Curve_js.csv',header=None).values

plt.plot(curve_js[:,0],label='1')
plt.plot(curve_js[:,1],label='2')
plt.plot(curve_js[:,2],label='3')
plt.plot(curve_js[:,3],label='4')
plt.plot(curve_js[:,4],label='5')
plt.plot(curve_js[:,5],label='6')
plt.legend()
plt.show()

