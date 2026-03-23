import pandas as pd
data={
    'Math':[90,85,80,95],
    'science':[88,82,85,90],
    'English':[78,75,80,85]
}
df=pd.DataFrame(data)
print("DataFrame:")
print(df)
corealation=df.corr()
print("\ncorrealation matrix\n",corealation)
