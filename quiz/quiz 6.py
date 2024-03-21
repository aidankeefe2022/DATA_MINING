import math

import numpy as np

S = [[2,0],[0,3]]

R = [[np.cos(np.pi/6),-np.sin(np.pi/6)],[np.sin(np.pi/6),np.cos(np.pi/6)]]

print(R)

y = np.matmul(R,S)

x = [[1,1]]

print(np.matmul(x,y))

print(math.sqrt(3)-1)
print()