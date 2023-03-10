import pandas as pd

# Load the CSV into a DataFrame:

df = pd.read_csv('Basic Pandas/data.csv')

# use to_string() to print the entire DataFrame.
print(df.to_string())
print("-------------------------------------------------")
print(df)
print("-------------------------------------------------")
print(pd.options.display.max_rows) 

# max_rows
# The number of rows returned is defined in Pandas option settings.

# You can check your system's maximum rows
# with the pd.options.display.max_rows statement