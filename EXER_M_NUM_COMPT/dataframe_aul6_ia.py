# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 23:05:48 2025

@author: Guglielmo H T
"""

import pandas as pd

df = pd.read_csv('csvFile.csv') #Carrega arquivo csv integro.
df1 = pd.DataFrame(df)
print(df1)

dfs = pd.read_csv('csvSujo2.csv') #Carrega arquivo csv sujo.
df2 = pd.DataFrame(dfs)
print(df2)


dfs.dropna(subset=['nome'], inplace=True) #exclui linha com valor inconsistente de 
#coluna nome.
dfl=pd.DataFrame(dfs)

print(dfl)

# Criando um DataFrame a partir de um dicionário
data = {
        'Coluna1': [1, 2, 3],
        'Coluna2': ['A', 'B', 'C'],
        'Coluna3':['Caneta',' ','Borracha']
        }
df3 = pd.DataFrame(data)



#print(df3['Coluna3'][0])
print(df3)



