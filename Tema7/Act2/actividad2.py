# matriz aleatoria entre 1 y 9 4x4
# Remplaza diagonal por primer num DNI
import numpy as np

array = np.random.randint(1, 9, size = (4, 4))
print('Array inicial: \n', array)

np.fill_diagonal(array, 3)
print('Diagonal modificada al primer número de mi DNI: \n', array)