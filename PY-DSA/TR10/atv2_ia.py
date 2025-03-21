# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 23:02:02 2025

@author: Guglielmo H T
"""

import numpy as np


valores=np.array([2,3,10,15,20])
soma=np.sum(valores)
minim=np.min(valores)
maxi=np.max(valores)
media=np.mean(valores)
raiz=np.sqrt(valores)

print(f"O valor da média é: {media}")
print(f"O valor da soma é: {soma}")
print(f"O menor valor é: {minim}")
print(f"O maior valor é: {maxi}")

print(raiz)

