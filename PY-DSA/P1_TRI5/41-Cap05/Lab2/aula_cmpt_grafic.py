

import numpy as np

# Define as coordenadas dos pontos
ponto_x = np.array([10, 20])  # Coordenadas (x, y) do ponto X
ponto_y = np.array([30, 40])  # Coordenadas (x, y) do ponto Y

# Calcula a diferença entre as coordenadas dos pontos
diferenca = ponto_y - ponto_x

# Calcula a distância euclidiana usando a norma L2
distancia = np.linalg.norm(diferenca)

print(f"A distância entre os pontos X e Y é: {distancia:.3f}")