
"""
Atividade Entregável 01-Métodos Numéricos Computacionais.

Escreva um programa que peça ao usuário dois valores numéricos:
um valor real exato e um valor aproximado. 
O programa deve calcular e exibir:O erro absoluto e o erro relativo

Fórmulas:
Erro Absoluto = | Valor Exato - Valor Aproximado |
Erro Relativo = (Erro Absoluto / | Valor Exato |)
PS: pode fazer em qualquer linguagem.
Prazo 25 de fev.

Prof: Leandro Oliveira da Silva
Aluno: Guglielmo Henriques Targino.
RA:2222104623.
Data: 17fev25
Versão: 01
"""

while True:  # loop para gantir que o valor digitdo seja um número exato.
    try:
        nreal = int(input("Por favor, digite um número inteiro: "))  
        break  # Sai do loop se for true
    except ValueError:  
        print("Entrada inválida! Digite um número inteiro válido.") 
        
        
while True:  # loop para garantir que o valor digitdo seja um númro aproximado.
    try:
        nfloat=float(input("Por favor digite um número aproximado."))  
        break  # Sai do loop se for true
    except ValueError:  
        print("Entrada inválida! Digite um número inteiro válido.") 
        
    
err_abs=abs(nreal-nfloat)
err_rel=err_abs/(abs(nreal))
print("erro absoluto é =", err_abs)
print("erro relativo é",err_rel)
    


