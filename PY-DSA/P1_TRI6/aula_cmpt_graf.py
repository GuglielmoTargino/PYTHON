import matplotlib.pyplot as plt
import numpy as np

def desenhar_figura(pontos_x, pontos_y, label):
    plt.plot(pontos_x, pontos_y, marker='o', label=label)

figuras = {
    "Triângulo": ([0, 1, 2, 0], [0, 2, 0, 0]),
    "Quadrado": ([0, 2, 2, 0, 0], [0, 0, 2, 2, 0]),
    "Pentágono": ([0, 1, 2, 2.5, 1.5, 0], [0, 2, 2, 1, -0.5, 0]),
    # Adicione outras figuras aqui
}

plt.figure(figsize=(8, 8))  # Define o tamanho do gráfico
for figura, (pontos_x, pontos_y) in figuras.items():
    desenhar_figura(pontos_x, pontos_y, figura)

plt.title('Figuras Geométricas em um Gráfico')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.grid(True)
plt.show()