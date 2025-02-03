import matplotlib.pyplot as plt
import pandas as pd
plt.switch_backend('TkAgg')

df=pd.read_csv('data.csv')
df['price_euros'] = df['price'] * 0.0121
df = df.dropna()

# Grafico de lineas
# Agrupar por marca y calcular los precios
precios_marca = df.groupby('brand')['price_euros'].mean()
# Crear un gráfico de líneas
precios_marca.plot(title='Precios según la marca', figsize=(10, 6))
plt.show()


# Grafico de dispresion
# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(
    df['brand'],
    df['price_euros'],
    alpha=0.6,
    c='blue',
    edgecolors='k'
)
plt.xticks(rotation=90) 
plt.title("Relación entre marca y precios", fontsize=14)
plt.xlabel("Marcas", fontsize=12)
plt.ylabel("Precios", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# Gráfico de barras
# Filtrar datos para la talla específica  
talla_especifica = '7'
df_talla = df[df['size'] == talla_especifica]
df_talla = df_talla.groupby('brand')['price_euros'].mean().reset_index()
# Crear un gráfico de barras
df_talla.plot(
    kind='bar',
    x='brand',
    y='price_euros',
    title=f'Precio por marca para la talla {talla_especifica}',
    figsize=(10, 6)
)
plt.show()


# Histograma
# Crear un histograma para los precios
df['price_euros'].plot(
    kind='hist',
    bins=20,
    title='Distribución de los precios',
    figsize=(10, 6)
)
plt.show()


# Diagrama de caja
# Crear un diagrama de caja para los precios por marca
plt.boxplot(
    df['price_euros'].dropna(),
    patch_artist=True,
    boxprops=dict(facecolor="lightblue", color="blue"),
    medianprops=dict(color="red"),
    flierprops=dict(marker="o", color="darkorange", markersize=5)
)
plt.title("Diagrama de caja: Precios")
plt.xlabel("Cantidad de precios")
plt.show()