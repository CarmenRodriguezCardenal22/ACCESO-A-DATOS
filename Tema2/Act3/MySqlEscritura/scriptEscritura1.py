import mysql.connector
import random
import time
start_time = time.time()
from mysql.connector import Error
try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='usuario',
        password='usuario',
        database='1dam'
    )
    cursor=conexion.cursor()
    ubi = ['España', 'Roma', 'París', 'Inglaterra', 'París']
    año = ['1506', '1670', '1450', '1800', '1331']
    estilo = ['Barroco', 'Contemporáneo', 'Clásico', 'Gótico', 'Renacentista']
    
    for i in range(0,10000):
        nombre = f"EdificiosHistoricos {i+1}"
        ubi = random.choice(ubi)
        año = random.choice(año)
        estilo = random.choice(estilo)
        cursor.execute(
            "INSERT into EdificiosHistoricos (nombre, ubicacion, añoContruccion, estiloArquitectonico) values (%s,%s,%s,%s)", 
            (nombre, ubi, año, estilo))
    
    if conexion.is_connected():
        print("Conexión a la base de datos exitosa")
except Error as e:
    print(f"Error de conexión: {e}")
finally:
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")
end_time = time.time()
print(f"Tiempo de inserción con mysql-connector: {end_time - start_time} segundos")
