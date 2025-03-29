# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 18:36:19 2025

@author: Guglielmo H T
"""

def interpolar_linear(min, x0, y0, x1, y1):
  return y0 + (y1 - y0) * ((min - x0) / (x1 - x0))

min=1.5 # variável tempo para estimativa da concentração desejada.
        #valor deve ficar entre 3 e 7. Pois são a faixa de valor confiável.
        #para teste de confiabilidade no cálculo, basta atribuir min com 
        # os valores 3 e 7. O resultado será como no enunciado.

# (min0, conc0) = (3, 8)
# (min1, conc1) = (7,20)
# (min, conc) = (5, 14) Obs: Valor obtido pelo método interpolação linear.

print(interpolar_linear(min, 1, 2, 3, 6))
