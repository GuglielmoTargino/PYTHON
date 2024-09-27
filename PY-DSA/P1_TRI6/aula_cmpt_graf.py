import matplotlib.pyplot as plt
import numpy as np

def desenhar_figura(pontos_x, pontos_y, label):
    plt.plot(pontos_x, pontos_y, marker='o', label=label)

figuras = {
    "Tri�ngulo": ([0, 1, 2, 0], [0, 2, 0, 0]),
    "Quadrado": ([0, 2, 2, 0, 0], [0, 0, 2, 2, 0]),
    "Pent�gono": ([0, 1, 2, 2.5, 1.5, 0], [0, 2, 2, 1, -0.5, 0]),
    # Adicione outras figuras aqui
}

plt.figure(figsize=(8, 8))  # Define o tamanho do gr�fico
for figura, (pontos_x, pontos_y) in figuras.items():
    desenhar_figura(pontos_x, pontos_y, figura)

plt.title('Figuras Geom�tricas em um Gr�fico')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.grid(True)
plt.show()