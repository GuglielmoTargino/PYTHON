# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:44:27 2024

@author: Guglielmo H T
"""

class Livro():
    def __init__(self,titulo,isbn):
        
        self.titulo=titulo
        self.isbn=isbn
        
        print("construtor chamado")
        
    def Imprime(self,titulo,isbn):
        print("Este é o livro %s e ISBN %d",titulo,isbn)
        





livro=Livro("primeiro POO em Python",7878)
print(livro.titulo)
print(livro.isbn)
        
        
        
        
        