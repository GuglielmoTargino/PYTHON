# -*- coding: utf-8 -*-
"""
Exercío aula oop while com listas DSA
Aluno:Guglielmo Targino
Data:16ago24
Versão: v0
"""

primo=[]

for num in range(2,10):
    
    # variavel de controle
    eh_primo=True
    
    
    # loop para verificar se o numero é primo
    i=2    
    while i<=num//2:
        
       
        if num %i==0: # e resto for 1 significa que não é primo
            eh_primo=False
            print (num)
            
            break
        i+=1
        
        
        # adiciona o numero na lista1 ggGGG
    if eh_primo:
        primo.append(num)
        
print(primo)
        
    



