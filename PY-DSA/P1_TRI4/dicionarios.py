# -*- coding: utf-8 -*-
"""
Aula do curso DSA com dicionários
Aluno: Guglielmo Targino
Data: 02ago24
Versão: v0

"""

dic1={'dara':0,'guga':1}; # 'dara' é a chave, 0 é o valor nessa chave
print(dic1);
gu=type(dic1);

print(gu);

gu=dic1['guga'];

print("A chave de guga é",gu);

dic1['nia']=8;
gu=dic1;

print(gu);

dic1.items();# retorna os itens
dic1.keys(); #retorna as chaves
dic1.values();# retorna os valores