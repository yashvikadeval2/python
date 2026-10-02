# .Write a Python program to find the mean, median, and mode of DataFrame columns

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],'Marks': [ 78, 92, 76 ,78 ,76]}
df = pd.DataFrame(data)

print("Mean:", df['Marks'].mean())
print("Median:", df['Marks'].median())
print("mode:",df['Marks'].mode())
