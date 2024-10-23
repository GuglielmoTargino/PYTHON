#execício com linguagem python do curso data Science Academy
#Treino com a função reduce

from functools import reduce


lista1=[2,3,4,85,6]

def somar(a,b):
   if (a>b):
       return a
   else:
       return b

res=reduce (somar,lista1)

print(res)

