#Trabalho final qld software.
#Aluno Guglielmo Targino.
#vers�o v1.
#Data 10nov24

import unittest

class Pessoa:
    def __init__(self,altura,peso):
             
        self.altura=altura
        self.peso=peso
      
         

    def calcImc(self):
        
        #verifica se algum valor de entrada � menor ou igual a zero.        
        if (self.altura):
            
            #f�rmula para c�lculo do imc
            return self.peso/(self.altura**2)
        else:
            return False
        

#prepara vari�veis para testes
alt=1.73 #variavel para altura
peso=73.6 #variavel para peso
esperado=24.59 #variavel para valor esperado

# Criando um objeto da classe Pessoa
pessoa1 = Pessoa(alt,peso)


#testes unit�rios inicia aqui.
class testeImc(unittest.TestCase):
    
    def test_imcIgual(self):
        #around arredondado para duas casas decimais
        #Aqui executa testes efetivos no m�todo calcImc().
        self.assertEqual(round(pessoa1.calcImc(),2),esperado)
        
        #aqui verifica o teste de valor igual a zero.
    def test_Falso(self):
        self.assertTrue(round(pessoa1.calcImc()),"Favor digitar n�meros maiores que 0.")
     
        #aqui verifica o teste de valor negativo.        
    def test_Neg(self):
         self.assertLess(round(pessoa1.calcImc()),0)
        

if __name__ == '__main__':
    unittest.main()

     
   