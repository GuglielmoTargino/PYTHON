#Atividade entregável 4 da disciplina QS.
#Aluno Guglielmo Targino.
#versão v1.
#Data 26set24

import unittest

def multiplicacao(a, b):
    return a * b
   

class mult(unittest.TestCase):
    def teste_Mult(self):
        self.assertEqual(multiplicacao(2.5, 8),20)#testa se o resultado é 20.
        self.assertEqual(multiplicacao(25, 2),50)#testa se o resultado é 50.
        self.assertEqual(multiplicacao(5, 8),40)#testa se o resultado é 40.
        self.assertEqual(multiplicacao(5, 9),45)#testa se o resultado é 43. Como 5x9=45, alerta sinal falso.
        self.assertFalse(multiplicacao(2.5, 0))#testa se o resultado é falso.
        self.assertTrue(multiplicacao(2.5, 0))#testa se o resultado é verdadeiro. Como 2.5x0=0. alerta sinal falso.
        

if __name__ == '__main__':
    unittest.main()
     
   