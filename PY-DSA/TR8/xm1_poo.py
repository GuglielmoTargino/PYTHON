# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:44:27 2024

@author: Guglielmo H T
"""

class Livro():
    def __init__(self):
        
        self.titulo="O grande Programador"
        self.isbn=7978
        
        print("construtor chamado")
        
    def Imprime(self):
        print(livro.titulo)
        print(livro.isbn)

class Carro():
    
    def __init__(self, a,b,c,d):
        self.nome=a
        self.ano=b
        self.cor=c
        self.motor=d
        
    def info(self):
        print(self.ano)
        print(self.motor)
        
        
livro=Livro()    
brava=Carro('Calebe',2000,'branco',1.6)

brava.info()
name=brava.nome
print(name)
lst={'guga',10}

print(lst)

resu=hasattr(livro,"titulo")
setattr(brava,'motor',1.8)
resu2=brava.motor

print(resu2)

        
        
        
        
        