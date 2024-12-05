# arrays 10 elementos valores entre 0 y 100
# filtra y muestra los mayores de 50
import numpy as np

array = np.random.randint(0, 100, size = (1, 10))
print('Array inicial: \n', array)

array50 = array[array>50]
print('Array filtrado con los números mayores que 50: \n', array50)