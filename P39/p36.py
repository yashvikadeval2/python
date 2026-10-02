#36.Write a Python program to remove duplicate records from a DataFrame.

import pandas as pd
a=[1, 2, 2, 3, 4, 4, 5]
s=set(a)
df=pd.DataFrame(s)
print(df)