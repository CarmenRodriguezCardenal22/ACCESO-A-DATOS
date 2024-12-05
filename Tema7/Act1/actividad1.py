# crear matriz de 0
# cambiar fila 1 a 1
#cambiar fila 2 a ul cifra dni
import numpy as np

array = np.zeros((3, 4))
print('Arrays inicial: \n', array)

array[0:1, 0:4] = 1
print('Primera fila modificada a 1: \n', array)

array[2:3, 0:4] = 3
print('Segunda fila modificada al último dígito de mi DNI: \n', array)