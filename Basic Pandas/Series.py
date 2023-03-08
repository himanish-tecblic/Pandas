# A Pandas Series is like a column in a table.

import pandas as pd

a = [10,22,13]

var = pd.Series(a)

print(var)
print("-------------------------------------------------------")


# -----------Labels-------------

# If nothing else is specified, the values are labeled
# with their index number. First value has index 0,
# second value has index 1 etc.

print(var[0])
print("-------------------------------------------------------")



# -----------Create Labels-------------

# With the index argument, you can name your own labels.

a = [10,22,13]

b = pd.Series(a, index = ["x", "y", "z"])

print(b)
print("-------------------------------------------------------")


print(b["y"])
print("-------------------------------------------------------")



# -----------Key/Value Objects as Series-------------

# You can also use a key/value object,
# like a dictionary, when creating a Series.

calories = {"day1": 420, "day2": 380, "day3": 390}

a1 = pd.Series(calories)

# Create a Series using only data from "day1" and "day2":

a2 = pd.Series(calories, index=["day1", "day2"])
print(a1)
print("-------------------------------------------------------")

print(a2)
print("-------------------------------------------------------")


# -----------DataFrames-------------

# Data sets in Pandas are usually multi-dimensional tables,
# called DataFrames.

# Series is like a column, a DataFrame is the whole table.

data = {
    "calories" : [420, 320, 390],
    "duration" : [50, 40, 45]
}

x = pd.DataFrame(data)
print(x)
print("-------------------------------------------------------")



