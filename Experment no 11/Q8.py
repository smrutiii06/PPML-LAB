import pandas as pd
df_csv=pd.read_csv("C:\\Users\\student\\Desktop\\24CSEAIML013\\Experment no 11\\sample.csv")
print(df_csv)
df_json=pd.read_json("C:\\Users\\student\\Desktop\\24CSEAIML013\\Experment no 11\\sample.json")
print("\nDataframe from JSON")
print(df_json)