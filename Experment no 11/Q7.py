import  pandas as pd
data={
    'Name':['Alice','Bob','charlie'],
    'Age':[25,30,35],
    'City':['new york','san francisco','los angeles']
}
df=pd.DataFrame(data)
print("Dataframe:")
print(df)
print("/nAge column:")
print(df['Age'])
print("/nRow at index 1:")
print(df.iloc[1])