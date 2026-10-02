# 37.Write a Python program to replace missing values with zero.

import pandas as pd
a=[1, 2, None, 3, 4, None, 5]
df=pd.DataFrame(a)
print(df.fillna(0))
# print(df)