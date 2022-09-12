# Author: Caio Rodrigues 
# Brief:  Test script for sample Python module mymodule 
#
#==================================================
import sarw_spheres as m
import numpy as np

print("\n ==== Call function: generateChain ====\n")

sizes = np.array([1.,1.,1.])
locations = np.zeros([4,3])

np.set_printoptions(suppress=True)
np.set_printoptions(precision = 2)

ret = m.generateChain(sizes)
print(ret)

print("\n\n==== End of Testing =========\n")
