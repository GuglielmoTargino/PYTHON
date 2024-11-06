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
        


palavra=['jaca','melao','abacaxi','vidro','agua','uva','jiboia','dara','nia']
segredo=random.choice(palavra)
print('Bem vindo ao jogo da forca')

chance=len(segredo)
revelacao=[]
print(segredo)
for x in segredo:
    revelacao.append('_')
    

print(chance)
print(revelacao)

cnt=0
pt=0



while cnt<chance:
    pt=0
    jogador=input('digite uma letra por favor')
    for x in segredo:
        if x==jogador:
            revelacao[pt]=jogador
            #print(revelacao)
            pt+=1
        else:
                      #revelacao[cnt]='_'
            #print(revelacao)j
            
            pt+=1
   
    cnt+=1
    print(revelacao)

    
print('perdeu')

    
    


   