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
    cursor.execute("select * from EdificiosHistoricos", )
    
    if conexion is not None:
        print("Conexión a la base de datos exitosa")
except MySQLError as e:
    print(f"Error de conexión: {e}")
finally:
    if conexion is not None:
        conexion.close()
        print("Conexión cerrada")
end_time = time.time()
print(f"Tiempo de lectura con PyMySql: {end_time - start_time} segundos")