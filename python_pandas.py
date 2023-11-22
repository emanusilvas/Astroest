'''
Pandas: Python DataFrames
'''

#%% Importando o pandas
import math as m
import matplotlib.pyplot as plt

import pandas as pd

#%% Criando uma estrutura de dados

dados = [[5.96, 7.86, 9.706, 11.007, 12.122],
         ['Ophi','Leo','Sgn','Vir','Cet'],
         [0.144, 0.090, 0.170, 0.168, 0.113],
         ['M4.0V', 'M6.0V', 'M3.5V', 'M5.5V'],
         [9.55, 13.44, 10.43, 11.13, 13.09],
         [13.22, 16.55, 10.43, 13.51, 15.26]]

colunas = ['Distancia', 'Constelacao', 'Massa',
           'Classe Espectral', 'mV', 'MV']

ids = ['Bernard', 'Wolf 359', 'Ross 154', 'Ross 128',
      'YZ Ceti']
           
#%% Criando um data frame
df1 = pd.DataFrame(dados)
    
print(df1, end='\n\n')
print(type(df1), end='\n\n')

    
#%% Atribuindo nomes para um dataframe
df2 = pd.DataFrame(dados).T
df2.columns = colunas

print(df2, end='\n\n')

#%% Atribuindo ids para linhas
df2.index = ids

print(df2, end='\n\n')

#%% Acessar valores do df
#df2[Massa]
#df2[['Massa', 'MV', 'mV']] (sub data frame)
#df2.mV
#df2.loc['Bernard']
#df2.iloc[0]

#%% Criando um sub df
df3 = df2[['Massa', 'MV', 'mV']]
print(df3, end='\n\n')

#%% Salvando um df
df2.to_latex('df2.txt') #Tabela tex
df2.to_csv('df2.csv') #Separado por virgula
df2[['Massa', 'MV']].to_csv('dfx.csv',
                            sep=' ',
                            header=False,
                            index=False) #Separa por espaço

#%% Outras utilidades
#df2.to_latex() (tabela em latex)