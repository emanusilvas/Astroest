'''
Analise Univariada
Dados: Sloan Digital Sky Survey - Realease 17

Emanuelly Silva
'''

#%% Importando os modulos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
#%% Leitura dos dados
fdata = "/home/maanubs/aulas/astroestatistica/data/SDSS-r17.csv"
df = pd.read_csv(fdata)

#%% Data cleaning?
print(f"Numero de NaNs: {df.isnull().sum()}")
print(f"Entradas repetidas: {df.duplicated().sum()}")

#%% Filtrando os dados
cols = ['alpha', 'delta', 'u', 'g', 'r', 'i', 'z',
        'class', 'redshift', 'MJD']

filtro1 = (df['u'] < 0) | (df['g'] < 0) | (df['z'] < 0 )
print(f"Celulas contendo magnitudes < 0: {filtro1.sum()}")

df = df[~filtro1]

#%% Explorando os dados
#%% Estatisticas basicas
print(df.describe(), end='\n\n')
stat = df[cols].describe()

# Percentil: tantos % menor que x valor
stat2 = df[cols].describe(percentiles=[0.01, 0.10, 0.50, 0.90, 0.99])

# Visualizacao dos dados
with pd.option_context('display.max_columns', 40):
    print(df[cols].describe())

#%% Histogramas
#%%
mode = 3
nbins = int(np.sqrt(len(df)))
#nbins = 20

#%%
#Utilizando funcoes graficas do pandas
if mode == 1:
    #df.hist()
    df[cols].hist(xlabelsize=7,
                  ylabelsize=7,
                  bins=nbins)
    plt.tight_layout()
    plt.show()

#Histogramas individuais (matplotlib)
elif mode == 2:
    for c in cols:
        plt.hist(df[c],
                 bins=nbins)
        plt.xlabel(c)
        plt.ylabel("Counts")
        plt.title(f"Histogram of {c}")
        plt.show()
        
#Histogramas via seaborn
elif mode == 3:
    for c in cols:
        sb.histplot(data=df[c])
        plt.xlabel(c)
        plt.ylabel("Counts")
        plt.title(f"Histogram of {c}")
        plt.show()
        
#%% Curvas de densidade

for c in cols:
    sb.kdeplot(data=df, x=c)
    #plt.xlabel(c)
    #plt.ylabel("Counts")
    #plt.title(f"Histogram of {c}")
    
    plt.show()  
        
    
