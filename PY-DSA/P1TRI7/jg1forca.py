#jogo em python da forca 
# https://docs.python.org/3.9/library/re.html
#Aluno:GuglielmoTargino.
#Dta:05nov24
#versão:v0.


import random
from os import name, system

def limpa_tela():
    if name == 'nt':
        system("cls")  # Windows
   
    else:
        system("clear")  # Linux/Mac
        

palavra=['jaca','agua','uva','dara','nia']
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
lb=0
bt=0



while cnt<chance:
    lb=0
    pt=0
    jogador=input('Digite Uma letra por favor_')
    for x in segredo:
        if x==jogador:
            revelacao[pt]=jogador
            pt+=1
        else:            
            pt+=1
   
    cnt+=1
    print(revelacao)  
    print(f'Você tem {chance-cnt} chances')
    
    for y in segredo:
        if segredo[lb]==revelacao[lb]:
            
            bt+=1
            print('IGUAL')
        else:
            bt=0
            print('NAO IGUAL')            
        lb+=1
        
        if bt==chance:
            print('VOCE GANHOU!')
        
    
            
      
    
print('FIM')

    
    


   