# array de 50 valores con linspace entre -1 y 1
# calcula el seno y muestra los array
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 50)
print('Array inicial: \n', x)

y = np.sin(x)
print('Array de senos: \n', y)