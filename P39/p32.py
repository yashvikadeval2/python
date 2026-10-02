# 32. Write a Python program to replace missing (NaN) values with the mean of the array.

import numpy as np
a=np.array([1,2,np.nan,4,5,np.nan,7,8])
print(a)
v = np.nanmean(a)
a[np.isnan(a)] = v
print(a)