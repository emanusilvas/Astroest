'''
Data cleaning - demonstraçao
'''

#%%Importando modulos
import pandas as pd

#%%Leitura dos dados
fdata = "/home/maanubs/aulas/astroestatistica/data/Cardio.csv"

df = pd.read_csv(fdata,
                 comment='#',
                 header=None)

#%% Renomeando colunas
df.columns = ['Duration', 'Date', 'Pulse', 'MaxPulse', 'Calories']

#%% Inspecionar dados
print(df)
print(df.head()) #primeiras linhas
print(df.tail()) #ultimas linhas

#%% 1. Celulas vazia (Nan, NAs, None)
print(df.info())
print(df.isnull().sum())

#%% 1.a Removendo vazios
df1 = df.dropna()

#%% 1.b Substituindo pela media

xmed = df['Calories'].mean()
xmedian = df['Calories'].median()
print(f'Media = {xmed}\nMediana = {xmedian}')

df2 = df.copy()
x = df2['Calories'].fillna(xmed, inplace=True)

df3 = df.copy()
y = df3['Calories'].fillna(xmedian, inplace=True)

#%% 1.c Substituindo por um valor especifico

df2.loc[22, 'Date'] = "'2020/12/22'"
df2.loc[26, 'Date'] = f"'{df2.loc[26, 'Date']}'"

#%% 2. Celulas com valores errados ou outlines

MAX_DURATION = 120

for i in df2.index:
    if df2.loc[i, 'Duration'] > MAX_DURATION:
        df2.drop(i,inplace=True)
        
#%% 3. Localizando entradas duplicadas
print(df2.duplicated())
print(df2.loc[df2.duplicated()])

df2.drop_duplicates(inplace=True)
