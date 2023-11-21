"""
Data:06/09/23  - Aula 2
Arquivo: Operação com Vetores atv.py
Slide: Computação Gráfica aula 2

"""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([7, 5])
B = np.array([-9, 4])
resultado = A + B

x_min = min(0, A[0], B[0], resultado[0])
x_max = max(0, A[0], B[0], resultado[0])
y_min = min(0, A[1], B[1], resultado[1])
y_max = max(0, A[1], B[1], resultado[1])
# figura e um conjunto de eixos
fig, ax = plt.subplots()

# Plotar o vetor A
ax.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='blue', label='A')

# Plotar o vetor B
ax.quiver(0, 0, B[0], B[1], angles='xy', scale_units='xy', scale=1, color='orange', label='B')

# Plotar o vetor resultante
ax.quiver(0, 0, resultado[0], resultado[1], angles='xy', scale_units='xy', scale=1, color='green', label='Resultado')

# Definir os limites do gráfico
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Adicionar um rótulo ao gráfico
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')

# Adicionar uma legenda
ax.legend()

# Mostrar o gráfico
plt.grid()
plt.show()
print (resultado)