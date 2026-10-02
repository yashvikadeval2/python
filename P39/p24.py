#24. Write a Python program to insert an element at a specified position in an array.


import numpy as np

a=np.array([1,2,3,4,5,6,7])
print(a)

l=list(a)
l.insert(2,10)
a=np.array(l)
print(a)