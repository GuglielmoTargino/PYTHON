#Exercício DSA
#Aluno Guglielmo Targino.
#versão v0
#Data 17set24

import os

cont_texto="python é legal na DSA!"

arquivo=open(os.path.join('C:/Users/Guglielmo H T/Desktop/aula6_DSA.txt'),'w')

for palavra in cont_texto.split(" "):
    arquivo.write(palavra + ' ' + '\n')
arquivo.close()