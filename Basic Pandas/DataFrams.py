import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)


print(df) 
print("------------------------------------")

print(df.loc[0])
print("------------------------------------")

print(df.loc[[0, 1]])
print("------------------------------------")

a = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(a)
print("------------------------------------")
