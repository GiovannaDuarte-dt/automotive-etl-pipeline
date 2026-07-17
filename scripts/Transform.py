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

print('\nQuantidade de linhas após remover duplicados:') 
print(len(df)) 

print('\nDados após a limpeza:') 
print(df) 

print ('\nModelos antes da padronização') 
print(df['model'].unique())  

print ('\npadronizando modelos')
df ['model'] = df ['model'].str.title() 
print('modelos padronizados') 
print (df['model'].unique())

print ('padronização coluna de textos') 
coluna_texto = ["dealership",
    "brand",
    "model",
    "color",
    "city"]
for coluna in coluna_texto:
    df[coluna] = df[coluna].str.title() 
print ('colunas padronizadas') 
print (df) 
