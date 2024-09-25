#Exercício DSA
#Aluno Guglielmo Targino.
#versão v0
#Data 25set24

import unittest

def multiplicacao(a, b):
    return a * b
   

class mult(unittest.TestCase):
    def teste_Mult(self):
        self.assertEqual(multiplicacao(2, 8), 16)
        #self.assertTrue(multiplicacao(4, 6), 24)
        #self.assertTrue(multiplicacao(0, 5), 0)
        #self.assertTrue(multiplicacao(-2, 3), -6)
    
   
    

   


if __name__ == '__main__':
    unittest.main()
     
   