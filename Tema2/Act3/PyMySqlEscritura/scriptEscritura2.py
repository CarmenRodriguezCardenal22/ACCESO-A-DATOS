import pymysql
import random
import time
start_time = time.time()
from pymysql import MySQLError
try:
    conexion = pymysql.connect(
        host='localhost',
        user="usuario",
        password='usuario',
        db="1dam"
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
    
    if conexion is not None:
        print("Conexión a la base de datos exitosa")
except MySQLError as e:
    print(f"Error de conexión: {e}")
finally:
    if conexion is not None:
        conexion.close()
        print("Conexión cerrada")
end_time = time.time()
print(f"Tiempo de inserción con PyMySql: {end_time - start_time} segundos")