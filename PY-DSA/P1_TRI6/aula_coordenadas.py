#Exercício de aula cmpt grafica.
#Aluno Guglielmo Targino.
#versão v0
#Data 13set24

import numpy as np
import math

# Função para realizar a translação em 2D
def translacao_2d(ponto, deslocamento):
    ponto_homogeneo = np.array([ponto[0], ponto[1], 1])
    matriz_translacao = np.array([
        [1, 0, deslocamento[0]],
        [0, 1, deslocamento[1]],
        [0, 0, 1]
    ])
    novo_ponto_homogeneo = np.dot(matriz_translacao, ponto_homogeneo)
    novo_ponto = novo_ponto_homogeneo[:2]
    return novo_ponto

# Função para realizar a rotação em 2D
def rotacao_2d(ponto, angulo):
    angulo_rad = math.radians(angulo)
    matriz_rotacao = np.array([
        [math.cos(angulo_rad), -math.sin(angulo_rad)],
        [math.sin(angulo_rad),  math.cos(angulo_rad)]
    ])
    novo_ponto = np.dot(matriz_rotacao, ponto)
    return novo_ponto

# Posição inicial do robô
posicao_inicial = [6,8 ]

# Deslocamento para translação
deslocamento = [10,10]

# Nova posição após translação
nova_posicao = translacao_2d(posicao_inicial, deslocamento)
print(f"Nova posição após translação: {nova_posicao}")

# Rotação do robô em 90 graus
angulo_rotacao = 0
posicao_final = rotacao_2d(nova_posicao, angulo_rotacao)
print(f"Posição do robô após rotação de 90 graus: {posicao_final}")