import pandas as pd

df = pd.read_csv("data.csv")

print('Esta es la información que nos proporciona el shape')
print(df.shape)
print(df.shape[0])
print(df.shape[1])

print('\nEsta es la información que nos proporciona el head')
print(df.head()) 

print('\nEsta es la información que nos proporciona el info')
print(df.info()) 

print('\nEsta es la información que nos proporciona el describe')
print(df.describe()) 

print('\nEstos son los registros de la tabla')
zapatos = df[["brand", "size", "price", "offer_price"]]
print(zapatos.head())

print('\nNueva columna:')
df["price_euros"] = df["price"] * 0.0121
print(df.head())

print('\nZapatos con el precio mayor de 50€:')
mas_de_50 = df[df["price_euros"] > 50 ]
print(mas_de_50.head())

print('\nLimpiar la tabla de nulos')
print(df.head())
df_limpio = df.dropna() # Crear un nuevo DataFrame sin valores nulos
print(f"Filas antes: {df.shape[0]}")
print(f"Filas después: {df_limpio.shape[0]}")

print('\nRellenar valores nulos:')
print('Antes:')
print(df.head())
df["price"]= df["price"].fillna(5287)
df["offer_price"]= df["offer_price"].fillna(4516)
df["price_euros"]= df["price_euros"].fillna(df["price"]*0.0121)
print('\nDespués:')
print(df.head())

print('\nAgrupar por tallas:')
conteo_por_tallas = df.groupby("size").size()
print(conteo_por_tallas)
print('\nPromedio de precio por tallas:')
promedio_tallas = df.groupby("size")[["price_euros"]].mean()
print(promedio_tallas)