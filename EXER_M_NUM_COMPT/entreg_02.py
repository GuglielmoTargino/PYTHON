# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 09:29:29 2025

@author: Guglielmo H T
"""

# Correlação de pearson entre o tempo de estudo e a nota do aluno
import numpy as np

x = np.array([1, 2, 3, 4, 5,6]) # tempo de estudo
y = np.array([2, 5, 7, 4, 9,9]) # nota do aluno

r = np.corrcoef(x, y)[0, 1]

print("O valor do coeficiente e: ", r)