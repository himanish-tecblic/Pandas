# One of the most used method for getting a quick overview of the DataFrame, is the head() method.

# The head() method returns the headers and a specified number of rows, starting from the top.

import pandas as pd

df = pd.read_csv('Basic Pandas/data.csv')

print(df.head(10))
print("-------------------------------------------------")
print(df.head())

# There is also a tail() method for viewing the last rows of the DataFrame.

# The tail() method returns the headers and a specified number of rows, starting from the bottom.

print("-------------------------------------------------")

print(df.tail())