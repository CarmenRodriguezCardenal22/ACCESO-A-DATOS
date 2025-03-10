import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar el dataset
df = pd.read_csv("insurance.csv")

# Transformar la fecha en una variable numérica (días desde la primera fecha registrada)
df['bmi'] = pd.to_numeric(df['bmi'], errors='coerce')
df = df.dropna(subset=['bmi'])

# Seleccionar columnas necesarias
df = df[['bmi', 'charges']]

# Dividir en entrenamiento y test (80% entrenamiento, 20% test)
df_train = df.sample(frac=0.8, random_state=42)
df_test = df.drop(df_train.index)

# Variables predictoras y objetivo
X_train = df_train[['bmi']]
y_train = df_train['charges']
X_test = df_test[['bmi']]
y_test = df_test['charges']

# Modelo de regresión lineal simple
modelo_lineal = LinearRegression()
modelo_lineal.fit(X_train, y_train)

# Predicción
y_pred = modelo_lineal.predict(X_test)

# Evaluación del error
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
print(f'RMSE con Regresión Lineal Simple (Predictor: Bmi): {rmse:.2f}')

# Seleccionar 40 registros aleatorios 
di = np.random.choice(df_test.index, size=30, replace=False)
dt = df_test.loc[di].copy()
y_pred_sample = modelo_lineal.predict(dt[['bmi']])

# Crear gráfico con 30 personas seleccionadas
plt.figure(figsize=(12, 6))
plt.plot(range(len(dt)), dt['charges'], marker='o', color='blue', linestyle='--', label='Datos reales')
plt.plot(range(len(dt)), y_pred_sample, marker='x', color='red', linestyle='--', label='Predicción')
plt.title('Regresión Lineal Simple - Predictor: Bmi')
plt.xlabel('BMI')
plt.ylabel('Charges')
plt.grid(True)
plt.legend()
plt.show()