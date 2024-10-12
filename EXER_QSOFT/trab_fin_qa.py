#Trabalho final qld software.
#Aluno Guglielmo Targino.
#versão v1.
#Data 12out24

import unittest

class Pessoa:
    def __init__(self,altura,peso):
        self.altura=altura
        self.peso=peso

    def calcImc(self):
        #fórmula para cálculo do imc
        return self.peso/(self.altura**2)
        
# Criando um objeto da classe Pessoa
#prepara variáveis para testes
valor1=1.72 #variavel para alura
valor2=73.6 #variavel para peso
esperado=24.88 #variavel para valor esperado
pessoa1 = Pessoa(valor1,valor2)

#usando o método para calcular o imc e guarda o resultado 
#arredondado para duas casas decimais na variável imc
imc=pessoa1.calcImc()
imc=round(imc,2)

#mostra o resultado do imc formatado com duas casas decimais.
#print("Meu imc é {:.2f}".format(imc))
print(imc)

class testeImc(unittest.TestCase):
     
    def test_imcIgual(self):
        self.assertEqual(imc,esperado)
    def test_Falso(self):
        self.assertFalse(imc,"não é falso")
        

if __name__ == '__main__':
    unittest.main()

     
   