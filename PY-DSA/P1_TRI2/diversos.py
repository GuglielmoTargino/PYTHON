# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 19:50:23 2024

@author: Guglielmo H T
Vesion: v0
"""

dados = [12, 15, 14, 10, 8, 12, 14, 10, 10, 15, 18, 12, 12, 14, 15, 16, 15, 10, 12]

 

import statistics
media = statistics.mean(dados)

variancia = statistics.variance(dados)
desvio_padrao = statistics.stdev(dados)

import numpy as np
q1 = np.percentile(dados, 25)
q3 = np.percentile(dados, 75)


print(q3)
print(q1)
print(variancia)
print(desvio_padrao)

x=0.154

print(f"Equação ajustada:{variancia:.2f}")
print(f"Equação ajustada:{desvio_padrao:.2f}")

alturas = [160, 165, 170, 175, 180, 185, 190, 195, 200]
pesos = [55, 60, 68, 72, 80, 85, 90, 95, 100]


correlacao = np.corrcoef(alturas, pesos)[0, 1]

print(correlacao)

print(f"Correlação person:{x:.2f}")
