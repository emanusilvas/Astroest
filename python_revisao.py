'''
Revisao sobre a linguagem Python
'''

#%%
#Palavras reservadas do Python
help('keywords')

#%%
#Tipos basicos de dados
#int:
#float:
#complex:
print(type (10), type (10.12), type (1+5j))

#%%
#Identificadores (variaveis)
# - primeiro caracter: letra ou _
# - seguido de quaisquer outros caracteres
# -  nao usar palavras reservadas do Python

A = 10
B = 10
c10 = 1.12
_abc = 3.12

#%%
# f~string
print(A, B, c10, sep='; ', end='\n\n')
print(A, B, c10, sep='\t ')

print(f" A = {A};\n B = {B};\n c10 = {c10}")

#%%
import math as m
from math import cos
from math import *

print( m.cos(0.5))

#%%
#Estruturas de repetiçao

obj = [1,2,3]
for e in obj:
    print(f"e={e}")
    
lista = [e*4 for e in range (0,11)]
for e in lista: print(e)

cont = 0
while cont <= 10:
    #if cont == 8: break (para parar antes)

    print(f"cont = {cont}")
    cont +=1

#%%
#Estruturas de decisao

x = 10
p=None

#Uma forma
if x%2==0:
    p = 'par'
else:
    p = 'impar'
print(f"{x} - {p}")

#Outra forma
j = 'par' if x%2==0 else 'impar'
print(f"{x} - {p}")

#%%
#list/tuple

import matplotlib.pyplot as plt

lista = {10,20,30}

x = [e/10 for e in range(-101,102)]
y = [e**3 for e in x]

print(x, y)
plt.plot(x, y)
plt.show()

tupla1 = (10,20,30) #nao pode ser alterada

#%%
#Dicionarios

destrela = {'Name': 'Sirius', 'magV': -1, 'magB': 0.5,
            'magU': 0.1, '(U-B)': 0.1-(-0.5),
            '(B-V)': 0.5-(-1)}

print(destrela)

for i in destrela:
    print(i)
    
for i in destrela.items():
    print(i)

for i in destrela.keys():
    print(i)
    
for i in destrela.values():
    print(i)

for i in destrela.items():
    print(f"{i[0]} \t: {i[1]}")

#%%
#Conjuntos

set1 = {1,5,7,18,23}
set2 = {1,23,10,20,30}

#Podemos explorar comandos como: set1 &set2, set1|set2
