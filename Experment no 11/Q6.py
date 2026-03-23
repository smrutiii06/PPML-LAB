import pandas as pd
data=[10,20,30]
labels=['a','b','c']
series=pd.Series(data,index=labels)
print("pandas Series:")
print(series)
print("values at label'b':",series['b'])