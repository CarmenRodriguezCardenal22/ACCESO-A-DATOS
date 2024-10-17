import mysql.connector
from mysql.connector import Error
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="usuario", 
        password="usuario", 
        db="1dam" 
    )
    cursor = conexion.cursor()
    cursor.callproc("contar_edificios")
    for resultado in cursor.stored_results():
        print(resultado.fetchall())
except Error as e:
    print(f"Error en la transacción: {e}")
    if conexion:
        conexion.rollback()
        print("Se realizó rollback.")
finally:
    if conexion and conexion is not None:
        cursor.close()
        conexion.close()
        print("Conexión cerrada.")