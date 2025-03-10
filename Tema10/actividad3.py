import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

# Cargar el dataset
df = pd.read_csv("insurance.csv")

# Convertir 'bmi' a tipo numérico
df['bmi'] = pd.to_numeric(df['bmi'], errors='coerce')

# Eliminar filas con valores nulos en 'bmi'
df = df.dropna(subset=['bmi'])

# Definir variable predictora y objetivo
X = df[['bmi']]
y = df['charges']

# Dividir en entrenamiento y test (80% entrenamiento, 20% test)
X_train = X.sample(frac=0.8, random_state=42)
y_train = y.loc[X_train.index]
X_test = X.drop(X_train.index)
y_test = y.drop(X_train.index)

# Modelo XGBoost para regresión
modelo_xgb = XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, random_state=42)
modelo_xgb.fit(X_train, y_train)

# Predicción
y_pred = modelo_xgb.predict(X_test)

# Evaluación del error
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
print(f'RMSE con XGBoost (Predictor: BMI): {rmse:.2f}')

# Seleccionar 30 registros aleatorios para graficar
di = np.random.choice(X_test.index, size=30, replace=False)
dt = X_test.loc[di].copy()
y_pred_sample = modelo_xgb.predict(dt)

# Crear gráfico con 30 registros seleccionados
plt.figure(figsize=(12, 6))
plt.plot(range(len(dt)), y.loc[di], marker='o', color='blue', linestyle='--', label='Datos reales')
plt.plot(range(len(dt)), y_pred_sample, marker='x', color='red', linestyle='--', label='Predicción')
plt.title('Regresión XGBoost - Predictor: BMI')
plt.xlabel('BMI')
plt.ylabel('Charges')
plt.grid(True)
plt.legend()
plt.show()
