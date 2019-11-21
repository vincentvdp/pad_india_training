import pandas as pd


sr = pd.Series([1,2,3,4,5,6,7])

print(type(sr))
print([x for x in sr if x<3])
