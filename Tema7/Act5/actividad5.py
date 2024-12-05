# array de 20 elementos aleatorios entre 0 y 50
# reestructurar en un array de 4x5
# calcular la suma de cada columna
import numpy as np

array = np.random.randint(0, 50, size = (1, 20))
print('Array inicial: \n', array)

nuevo_array = array.reshape((4, 5))
print('Array reestructurado: \n', nuevo_array)

print('Suma por columnas: \n', nuevo_array.sum(axis=0))
