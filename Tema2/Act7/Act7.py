import mysql.connector
from mysql.connector import Error
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="usuario", 
        password="usuario", 
        db="1dam" 
    )
    if conexion is not None:
        cursor = conexion.cursor()
        print("Iniciando transacción...")
        sql_insert = """
            INSERT INTO EdificiosHistoricos (nombre, ubicacion, añoContruccion, estiloArquitectonico)
            VALUES (%s, %s, %s, %s)
        """
        datos_herramienta = ("Giralda", "España", "10/06/1879", "Renacentista")
        cursor.execute(sql_insert, datos_herramienta)
        conexion.commit()
        print("Transacción exitosa: Registro insertado correctamente.")
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
