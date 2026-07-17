import pandas as pd 

print('Aprendendo a primeira etapa de limpeza de dados')

df = pd.read_csv("data/raw/sales_2025_01.csv")

print("Dados carregados")
print(df.head()) 

print("\nDuplicados considerando dados de vendas:")
print(df.duplicated (
    subset=["date", "dealership", "brand", "model", "color", "price", "city"]
).sum())

df.drop_duplicates(
    subset=["date", "dealership", "brand", "model", "color", "price", "city"],
inplace=True
 )

print('\nQuantidade de linhas após remover duplacados:') 
print(len(df)) 

print('\nDados após a limpeza:') 
print(df) 