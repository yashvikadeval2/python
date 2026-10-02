# 30. Write a Python program to shuffle the elements of an array.

import numpy as np
a=np.array([1,2,3,4,5,6,7,8 ])
print(a)
np.random.shuffle(a)
print(a)