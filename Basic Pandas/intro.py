import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

a = pd.DataFrame(mydataset)

print(a)
print(pd.__version__)