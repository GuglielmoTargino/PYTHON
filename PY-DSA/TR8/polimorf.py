# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:44:27 2024

@author: Guglielmo H T
"""

class Animal:       
    
    def __init__(self, som,move):
        
        self.som=som
        self.move=move
        
    def Soar(self):
        pass

class Gato(Animal):
    
    def Soar(self):
        print("Gato mia")
        print(self.som)
        
class Cachorro(Animal):
    
    def Soar(self):
        
        print("Cachorro late")
               
               
        

lic=Gato("mia","pula")
print(lic.som)




        
        
        
        
        