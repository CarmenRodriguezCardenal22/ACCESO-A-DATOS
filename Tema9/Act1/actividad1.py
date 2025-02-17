import pandas as pd

df = pd.read_csv("data.csv")
df["price_euros"] = df["price"] * 0.0121

#Transformar las variables categóricas a numéricas
df_encoded_brand = pd.get_dummies(df, columns=["brand"], drop_first=False)
df_encoded_color = pd.get_dummies(df, columns=["color"], drop_first=False)

#Calcular la correlación entre las variables numéricas
print(df[['df_encoded_brand','price_euros']].corr())
print(df[['size', 'price_euros']].corr())
print(df[['df_encoded_color', 'price_euros']].corr())