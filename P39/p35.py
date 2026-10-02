# 35. Write a Python program to find students who scored more than 80 marks using Pandas.

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],'Marks': [85, 78, 92, 88, 76]}
df = pd.DataFrame(data)
print(df[df['Marks'] > 80])
