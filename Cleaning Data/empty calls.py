# Empty cells can potentially give you a wrong result when you analyze data.


import pandas as pd

df = pd.read_csv('Cleaning Data/data.csv')

print(df.to_string())
print("----------------------------------")
# a = df.dropna()
df.dropna(inplace = True)
print("----------------------------------")
# print(a.to_string())
print(df.to_string())