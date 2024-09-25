#Atividade entregável 4 da disciplina QS.
#Aluno Guglielmo Targino.
#versão v0
#Data 25set24

import unittest

def multiplicacao(a, b):
    return a * b
   

class mult(unittest.TestCase):
    def teste_Mult(self):
        self.assertEqual(multiplicacao(2.5, 8),20)
        
    def teste_Mult2(self):
        self.assertEqual(multiplicacao(5, 8),40)

if __name__ == '__main__':
    unittest.main()
     
   