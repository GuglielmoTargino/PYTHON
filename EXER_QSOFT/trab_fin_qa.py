#Trabalho final qld software.
#Aluno Guglielmo Targino.
#vers�o v1.
#Data 12out24

import unittest

class Pessoa:
    def __init__(self,altura,peso):
        self.altura=altura
        self.peso=peso

    def calcImc(self):
        #f�rmula para c�lculo do imc
        return self.peso/(self.altura**2)
        
# Criando um objeto da classe Pessoa
#prepara vari�veis para testes
valor1=1.72 #variavel para alura
valor2=73.6 #variavel para peso
esperado=24.88 #variavel para valor esperado
pessoa1 = Pessoa(valor1,valor2)

#usando o m�todo para calcular o imc e guarda o resultado 
#arredondado para duas casas decimais na vari�vel imc
imc=pessoa1.calcImc()
imc=round(imc,2)

#mostra o resultado do imc formatado com duas casas decimais.
#print("Meu imc � {:.2f}".format(imc))
print(imc)

class testeImc(unittest.TestCase):
     
    def test_imcIgual(self):
        self.assertEqual(imc,esperado)
    def test_Falso(self):
        self.assertFalse(imc,"n�o � falso")
        

if __name__ == '__main__':
    unittest.main()

     
   