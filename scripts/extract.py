import pandas as pd 
df = pd.read_csv("data/raw/sales_2025_01.csv")
print (df.head()) 
print("\nInformações do DataFrame:")
print(df.info())

print("\nEstatísticas:")
print(df.describe())

print("\nValores nulos:")
print(df.isnull().sum())