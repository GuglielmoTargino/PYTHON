# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 09:29:29 2025

@author: Guglielmo H T
"""

# Correlação de pearson entre o tempo de exercício por dia e perda de peso do atleta.
# Estudo teórico avaliando 10 atletas durante 30 dias.
import numpy as np

hora = np.array([0.2, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]) # horas de exercício
peso = np.array([0.1, 0.3, 0.3, 0.6, 0.8, 0.8,0.8,0.9,1]) #perda de peso em kg

r = np.corrcoef(hora,peso)[0, 1]

print(f"O valor do coeficiente e:{r:.3f} ")

import matplotlib.pyplot as plt

plt.scatter(hora,peso)
plt.xlabel("Tempo de exercício em horas por dia")
plt.ylabel("Perda de peso em kg")
plt.title("Correlação entre Tempo de exercício e perda de peso")
plt.show()