# -*- coding: utf-8 -*-
"""
#Aula DSA tr6.Manipulação de dados csv
#Aluno Guglielmo Targino.
#versão v0
#Data 03out24
"""
import csv

with open('C:/Users/Guglielmo H T/Desktop/lista.csv','w') as arquivo:
    conteudo=csv.writer(arquivo)
    conteudo.writerow(('nota1','nota2','nota3'))
    conteudo.writerow(('5','7','10'))
    conteudo.writerow(('8','8','9'))
    
with open('C:/Users/Guglielmo H T/Desktop/lista.csv','r', encoding='utf8', newline='\r\n') as arquivo:
      leitor=csv.reader(arquivo)
      dados=list(leitor)
      
      
      
print(dados)
    
    