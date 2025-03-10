import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar el dataset
df = pd.read_csv("insurance.csv")

# Convertir la columna 'smoker' a valores numéricos (0 = no fumador, 1 = fumador)
df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})

# Seleccionar columnas necesarias y convertirlas a tipo numérico
df[['bmi', 'age']] = df[['bmi', 'age']].apply(pd.to_numeric, errors='coerce')

# Eliminar outliers utilizando el método IQR
Q1 = df[['bmi', 'age', 'smoker']].quantile(0.25)
Q3 = df[['bmi', 'age', 'smoker']].quantile(0.75)
IQR = Q3 - Q1

# Filtrar outliers
df_no_outliers = df[~((df[['bmi', 'age', 'smoker']] < (Q1 - 1.5 * IQR)) | (df[['bmi', 'age', 'smoker']] > (Q3 + 1.5 * IQR))).any(axis=1)]

# Definir variables predictoras y objetivo
X = df_no_outliers[['bmi', 'age', 'smoker']]
y = df_no_outliers['charges']

# Dividir en entrenamiento y test (80% entrenamiento, 20% test)
X_train = X.sample(frac=0.8, random_state=42)
y_train = y.loc[X_train.index]
X_test = X.drop(X_train.index)
y_test = y.drop(X_train.index)

# Modelo de regresión lineal múltiple
modelo_multiple = LinearRegression()
modelo_multiple.fit(X_train, y_train)

# Predicción
y_pred = modelo_multiple.predict(X_test)

# Evaluación del error
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
print(f'RMSE con Regresión Lineal Múltiple (sin outliers): {rmse:.2f}')

# Seleccionar 30 registros aleatorios
di = np.random.choice(X_test.index, size=30, replace=False)
dt = X_test.loc[di].copy()
y_pred_sample = modelo_multiple.predict(dt)

# Crear gráfico con 30 registros seleccionados
plt.figure(figsize=(12, 6))
plt.plot(range(len(dt)), y.loc[di], marker='o', color='blue', linestyle='--', label='Datos reales')
plt.plot(range(len(dt)), y_pred_sample, marker='x', color='red', linestyle='--', label='Predicción')
plt.title('Regresión Lineal Múltiple - Predicción de Charges (sin outliers)')
plt.xlabel('BMI, Age, Smoker')
plt.ylabel('Charges')
plt.grid(True)
plt.legend()
plt.show()
