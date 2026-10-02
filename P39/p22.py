#. Write a Python program to create a two-dimensional array of size 3 × 4 and display its shape and dimensions.

import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print(np.shape(a))
print(np.ndim(a))