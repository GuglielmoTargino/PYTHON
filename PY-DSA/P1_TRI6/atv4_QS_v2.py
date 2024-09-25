# -*- coding: utf-8 -*-
"""
#Atividade entregável 4 da disciplina QS.
#Aluno Guglielmo Targino.
#versão v2
#Data 25set24
"""

import unittest

def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma_positiva(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativa(self):
        self.assertEqual(soma(-2, 3), 1)

if __name__ == '__main__':
    unittest.main()