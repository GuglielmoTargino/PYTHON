#Trabalho final qld software.
#Aluno Guglielmo Targino.
#versão v1.
#Data 17out24

import unittest

class Pessoa:
    def __init__(self,altura,peso):
             
        self.altura=altura
        self.peso=peso
      
         

    def calcImc(self):
        
        #verifica se algum valor de entrada é menor ou igual a zero.        
        if (self.altura and self.peso):
            
            #fórmula para cálculo do imc
            return self.peso/(self.altura**2)
        else:
            return False
        

#prepara variáveis para testes
alt=0.62 #variavel para altura
peso=595 #variavel para peso
esperado=1547.87 #variavel para valor esperado

# Criando um objeto da classe Pessoa
pessoa1 = Pessoa(alt,peso)


#testes unitários inicia aqui.
class testeImc(unittest.TestCase):
     
    def test_imcIgual(self):
        #around arredondado para duas casas decimais
        #Aqui executa testes efetivos no método calcImc().
        self.assertEqual(round(pessoa1.calcImc(),2),esperado)
        
        #aqui verifica o teste de valor inferior ou igual a zero foi digitado.
    def test_Falso(self):
        self.assertTrue(round(pessoa1.calcImc()),"Por favor digite numeros positivos.")
        

if __name__ == '__main__':
    unittest.main()

     
   