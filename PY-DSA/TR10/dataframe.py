# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 18:36:19 2025

@author: Guglielmo H T
"""

def interpolar_linear(min, min0, conc0, min1, conc1):
  return conc0 + (conc1 - conc0) * ((min - min0) / (min1 - min0))

min=5 # variável tempo para estimativa da concentração desejada.
        #valor deve ficar entre 3 e 7. Pois são a faixa de valor confiável.
        #para teste de confiabilidade no cálculo, basta atribuir min com 
        # os valores 3 e 7. O resultado será como no enunciado.

# (min0, conc0) = (3, 8)
# (min1, conc1) = (7,20)
# (min, conc) = (5, 14) Obs: Valor obtido pelo método interpolação linear.

print(interpolar_linear(min, 3, 8, 7, 20))
