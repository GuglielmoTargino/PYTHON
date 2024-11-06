#jogo em python da forca 
# https://docs.python.org/3.9/library/re.html
#Aluno:GuglielmoTargino.
#Dta:05nov24
#versão:v0.


import random
from os import name, system

def limpa_tela():
    if name == 'nt2':
        system("cls")  # Windows
   
    else:
        system("clear")  # Linux/Mac
        
print('Bem vindo ao jogo da forca')

palavra=['jaca','melao','abacaxi','vidro','agua','uva','jiboia','dara','nia']

segredo=random.choice(palavra)
print(segredo)

for x in segredo:
    print('_')


   