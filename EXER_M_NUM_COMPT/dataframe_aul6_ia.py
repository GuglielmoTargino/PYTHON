# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 23:05:48 2025

@author: Guglielmo H T
"""

import pandas as pd

df = pd.read_csv('csvFile2.csv')

print(df)

df = pd.read_csv('csvSujo2.csv')
print(df)

df.dropna(subset=['nome'], inplace=True)

dframe=pd.DataFrame(df)

print(dframe)

# Criando um DataFrame a partir de um dicionário
data = {
        'Coluna1': [1, 2, 3],
        'Coluna2': ['A', 'B', 'C'],
        'Coluna3':['Caneta',' ','Borracha']
        }
df3 = pd.DataFrame(data)


print(df3['Coluna3'][0])
print(data)

