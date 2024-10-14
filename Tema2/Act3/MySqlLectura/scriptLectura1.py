import mysql.connector
import time
start_time = time.time()
from mysql.connector import Error
try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='usuario',
        password='usuario',
        db='1dam'
    )
    cursor = conexion.cursor()
    for i in range (0,10000):
        cursor.execute("select * from EdificiosHistoricos")
        cursor.fetchall()
except Error as e:
    print(f"Error de conexión: {e}")
finally:
    if conexion is not None:
        conexion.close()
        print("Conexión cerrada")
end_time = time.time()
print(f"Tiempo de lectura con mysql-connector: {end_time - start_time} segundos")
