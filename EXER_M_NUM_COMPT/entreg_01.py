# -*- coding: utf-8 -*-
"""
Atividade Entregável 01-Métodos Numéricos Computacionais.

Escreva um programa que peça ao usuário dois valores numéricos:
um valor real exato e um valor aproximado. 
O programa deve calcular e exibir:O erro absolutoO erro relativo

Fórmulas:
Erro Absoluto = | Valor Exato - Valor Aproximado |
Erro Relativo = (Erro Absoluto / | Valor Exato |)
PS: pode fazer em qualquer linguagem.
Prazo 25 de fev.

Prof: Leandro Oliveira da Silva
Aluno: Guglielmo Henriques Targino.
RA:2222104623.
Data: 25fev25
Versão: 01
"""

import numpy as npy

print(npy.__version__)

arr1=npy.array([10,12,13])
print(arr1[1])

print(type(arr1))
arr1[1]=500

print(arr1[1])
