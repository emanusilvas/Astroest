'''
Pandas: aplicacao e analise de dados
'''

#%% Coisas uteis p o codigo:
print2 = lambda titulo, obj : print(50*"=", "\n", titulo, 50*"=", "\n", obj, end="\n\n")
Msun = 2.e33 # massa solar em kg

#%% Importando o pandas:
import pandas as pd

#%% Ler dados de um arquivo CSV:
dir_data = "/home/maanubs/aulas/astroestatistica/data/"
fdata = dir_data + "Exoplanets_2023.10.24_08.34.54.csv"

df = pd.read_csv(fdata,
                 comment='#',
                 index_col=0)

#%% Examinar estrutura interna do dataframe:
#print(50*"=", "\n", "Data frame df:", 50*"=", "\n", df, end="\n\n")

show = False

if show:
    print2 ("Data frame df", df)
    print2 ("Colunas do df:", df.columns)
    print2 ("Indices das linhas:", df.index)
    
#%% Construindo um novo df somente c/ colunas de interesse:

cols = ['kepler_name', #star name (Kepler catalog.),
        'koi_smass',   #star mass
        'ra',          #Rigth ascension
        'dec',         #declination
        ]

#Cuidado fazer uma copia independente usando o metodo copy
df1 = df[cols].copy() #copia independente

#%% Alterando o nome das colunas no novo df:
mapper = {'kepler_name' : 'Name',
          'koi_smass' : 'Mass',
          'ra' : 'Ra',
          'dec' : 'DEC'}

df1.rename(columns = mapper, 
            inplace = True)

#%% Criando uma nova coluna no nosso df:
MassKg = df1['Mass'].values * Msun

df1["MassKg"] = MassKg

#%% Deletando colunas no df:
df1.drop(columns = "Name", inplace = True)

#%% Filtrar dados:
filtro1 = df1.Mass <= 0
filtro2 = df1.Mass.isna()
filtro3 = filtro1 | filtro2

df1_bad = df1[filtro3]
dfi_good = df1[~filtro3]

df1.plot(kind = 'scatter', x='Ra', y='DEC')
df1.hist(column = 'Mass', bins=30)
#bins: largura dos histogramas

