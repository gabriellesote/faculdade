'''
Data: 23/08/23 - Aula 1 - Atividade -

Calcule os seguintes pontos em numpy e modifique a quantidade
de casas decimais exibidas após a virgula para 2 casas:
A (3, 8), B (7, 12)
C (4, -3), D (-8, 9)
E (10, -9), F( -7, 0)
'''
import numpy as np


A = (3, 8)
B = (7, 12)
C = (4, -3)
D = (-8, 9)
E = (10, -9)
F = (-7, 0)

x1, y1 = A
x2, y2 = B

# Calcular a distância entre A e B
distancia_AB = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
distancia_AB = round(distancia_AB, 2)
print("A distância entre os pontos A e B é:", distancia_AB)


# Calcular a distância entre C e D
x1, y1 = C
x2, y2 = D
distancia_CD = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
distancia_CD = round(distancia_CD, 2)
print("A distância entre os pontos C e D é:", distancia_CD)

# Calcular a distância entre E e F
x1, y1 = E
x2, y2 = F
distancia_EF = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
distancia_EF = round(distancia_EF, 2)
print("A distância entre os pontos E e F é:", distancia_EF)
