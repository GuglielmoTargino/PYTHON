# -*- coding: utf-8 -*-
"""
#Aula DSA tr6.
#Aluno Guglielmo Targino.
#versão v0
#Data 03out24
"""
#with open('C:/Users/Guglielmo H T/Desktop/logue.txt','r') as arquivo:
   # conteudo=arquivo.read()
   # print(conteudo)
    
texto=' PYTHON E LEGAL DE MAIS'
with open('C:/Users/Guglielmo H T/Desktop/logue.txt','w') as arquivo:
   arquivo.write(texto[:19])
   arquivo.write('\n')
   arquivo.write(texto[2:6])