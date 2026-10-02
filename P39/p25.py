#25. Write a program to split a NumPy array into equal parts.

import numpy as np

a=np.array([1,2,3,4,5,6,7,8])
print(a)
print(np.array_split(a, 4))

