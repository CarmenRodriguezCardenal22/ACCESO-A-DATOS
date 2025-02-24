import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
import matplotlib.pyplot as plt

df = pd.read_csv("insurance.csv")
encoded = OrdinalEncoder()

print('Correlación de la edad con costo de seguro')
print(df[['charges','age']].corr())

print('\nCorrelación del sexo con costo de seguro')
df[['sex']] = encoded.fit_transform(df[['sex']])
df[['sex']] = df[['sex']].astype(int)
print(df[['charges', 'sex']].corr())

print('\nCorrelación del indice de peso corporal con costo de seguro')
print(df[['charges','bmi']].corr())

print('\nCorrelación del nº de hijos con costo de seguro')
print(df[['charges','children']].corr())

print('\nCorrelación de si es o no fumador con costo de seguro')
df[['smoker']] = encoded.fit_transform(df[['smoker']])
df[['smoker']] = df[['smoker']].astype(int)
print(df[['charges', 'smoker']].corr())

print('\nCorrelación de la region con costo de seguro')
df[['region']] = encoded.fit_transform(df[['region']])
df[['region']] = df[['region']].astype(int)
print(df[['charges', 'region']].corr())


# Identificacion de valores nulos
print('\nIdentificación de valores nulos')
dt = df[['charges','age','bmi','smoker']]
print(dt.isnull().sum())

# Identificación de valores erroneos
precio_edad = df.groupby('age')['charges'].mean()
precio_edad.plot(title='Costo de seguro por edad', figsize=(10,6))
plt.show()

precio_bmi = df.groupby('bmi')['charges'].mean()
precio_bmi.plot(title='Costo de seguro por bmi', figsize=(10,6))
plt.show()

otros_valores = df[df['smoker'].isin[('yes','no')]]
conteo_otros = otros_valores.shape[0]
print(f'Valores erroneos: {conteo_otros}')
