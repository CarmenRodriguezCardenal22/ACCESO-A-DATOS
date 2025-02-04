import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data.csv")
df["price_euros"] = df["price"] * 0.0121
df = df.dropna()

print('Eliminación de outliers')

#Calcular el rango intercuartil (IQR)
q1 = df["price_euros"].quantile(0.25) # Primer cuartil
q3 = df["price_euros"].quantile(0.75) # Tercer cuartil
print('Primer cuartil: ', q1, ', Tercer cuartil: ', q3)
iqr = q3 - q1 # Rango intercuartil
# Definir los límites inferior y superior
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print(f"Límite inferior: {lower_bound}, Límite superior: {upper_bound}")

# Filtrar valores dentro de los límites
df_sin_atipicos = df[(df["price_euros"] >= lower_bound) & (df["price_euros"] <=
upper_bound)]
# Comparar el número de filas antes y después
print(f"Filas antes: {df.shape[0]}")
print(f"Filas después de eliminar atípicos: {df_sin_atipicos.shape[0]}")

print('\nNormalización de la columna price_euros')
min = df["price_euros"].min()
max = df["price_euros"].max()
print(f" Mínimo precio en euros: {min}")
print(f" Máximo precio en euros: {max}")

# Normalizar las columnas
df["price_euros_norm"] = (df["price_euros"] - min) / (max - min)
# Mostrar los resultados
print(df[["price_euros", "price_euros_norm"]].head())

print('\nDatos antes de One-Hot Encoding')
print(df[["brand", "color"]].head())

# Aplicar One-Hot Encoding a la columna "color"
df_encoded = pd.get_dummies(df, columns=["color"], drop_first=False)
# Mostrar un ejemplo de los datos codificados
print("\nDatos después de One-Hot Encoding:")
print(df_encoded[["brand", "color_Red", "color_Blue", "color_Black", "color_Gold", "color_Yellow"]].head())

print('\nSeparar columnas predictoras y objetivo')
# Variables predictoras
X = df[["brand", "color", "size"]]
# Variable objetivo
y = df["price_euros"]

print('Variables predictoras: \n', X.head())
print('Variables objetivo: \n', y.head())

print('\nSeparar datos de entrenamiento y prueba')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=42)
# Mostrar resultados
print("Tamaño del conjunto de entrenamiento:", X_train.shape[0])
print("Tamaño del conjunto de prueba:", X_test.shape[0])
print('Conjunto de entrenamiento: \n', X_train.head())
print('Conjunto de prueba: \n', X_test.head())
print('Conjunto de entrenamiento (objetivo): \n', y_train.head())
print('Conjunto de prueba (objetivo): \n', y_test.head())

print('\nFunción personalizada')
# Función personalizada para determinar el resultado
def calcular_descuento(row):
    return (row["price"] - row["offer_price"]) / row["price"] * 100
# Aplicar la función a cada fila
df["descuento(%)"] = df.apply(calcular_descuento, axis=1)
# Mostrar un ejemplo
print(df.head())

print('\nUnir DataFrames')
# Crear un DataFrame adicional con información de las regiones de las tallas
paises_data = {
    "size": ["1", "40", "UK-09"],
    "country": ["EEUU", "España", "Reino Unido"],
}
paises_df = pd.DataFrame(paises_data)

# Unir la talla al pais
df_merged = df.merge(paises_df, on="size", how="inner")
df_merged = df_merged.rename(columns={"country": "paises"})

# Mostrar los primeros 5 resultados con las regiones
print(df_merged[["brand", "color", "size", "paises"]])