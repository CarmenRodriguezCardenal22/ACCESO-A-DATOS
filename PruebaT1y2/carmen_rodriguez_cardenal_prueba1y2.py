import pymysql
from pymysql import MySQLError
import json
import csv
try:
    # Abrimos conexión con la base de datos
    conexion = pymysql.connect(
        host="localhost", 
        user="usuario", 
        password="usuario", 
        db="1dam"
    )
    cursor = conexion.cursor()
    # Creación de la tabla Libros
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Libros(
        titulo VARCHAR(50) PRIMARY KEY,
        autor VARCHAR(50),
        genero VARCHAR(50),
        año_publicacion VARCHAR (50),
        libreria_origen VARCHAR (50)
    );
    """)
    # Inserción de los datos en la tabla
    cursor.execute(
        "INSERT INTO Libros (titulo, autor, genero, año_publicacion, libreria_origen) VALUES (%s, %s, %s, %s, %s)",
        ('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Novela', '1605', 'Ramón Valle Inclán')
    )
    cursor.execute(
         "INSERT INTO Libros (titulo, autor, genero, año_publicacion, libreria_origen) VALUES (%s, %s, %s, %s, %s)",
        ('Cien Años de Soledad', 'Gabriel García Márquez', 'Novela', '1967', 'Ramón Valle Inclán')
    )
    cursor.execute(
         "INSERT INTO Libros (titulo, autor, genero, año_publicacion, libreria_origen) VALUES (%s, %s, %s, %s, %s)",
        ('Crimen y Castigo', 'Fiódor Dostoyevski', 'Novela', '1866', 'Ramón Valle Inclán')
    )
    cursor.execute(
         "INSERT INTO Libros (titulo, autor, genero, año_publicacion, libreria_origen) VALUES (%s, %s, %s, %s, %s)",
        ('La Casa de los Espíritus', 'Isabel Allende', 'Novela', '1982', 'Ramón Valle Inclán')
    )
    cursor.execute(
         "INSERT INTO Libros (titulo, autor, genero, año_publicacion, libreria_origen) VALUES (%s, %s, %s, %s, %s)",
        ('El Nombre de la Rosa', 'Umberto Eco', 'Misterio', '1980', 'Ramón Valle Inclán')      
    )
    conexion.commit()
    if conexion is not None:
        # Mostrar los datos de la tabla
        print("Tabla creada con exito")
        cursor.execute("SELECT * FROM Libros")
        for fila in cursor.fetchall():
            print(fila)
except MySQLError as e:
    print(f"Error de conexión: {e}")
        

class JSONFileHandler:  
    # Escritura de la base de datos en un fichero Json
    def write_json(self, file_path):
        try:
            d = cursor.execute("SELECT * FROM Libros")
            with open(file_path, 'w') as f:
                json.dump(d,f)
            print('Hay un total de ', d, 'datos introducidos en la base de datos')
        except Exception as e:
            print(f"Error escribiendo JSON: {e}")  
    # Lectura de un fichero Json
    def read_json(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error leyendo JSON: {e}")
            
print('Datos del fichero JSON')
json_handler = JSONFileHandler()
data = json_handler.read_json('libros_machado.json')
print(data, 'libreria_origen: Antonio Machado')




# Lectura de un fichero CSV
class CSVFileHandler:
    def read_csv(self, file_path):
        try:
            with open(file_path, mode='r', newline='') as f:
                reader = csv.DictReader(f) 
                rows = [] 
                for row in reader:
                    rows.append(row)
                return rows 
        except Exception as e:
            print(f"Error leyendo el archivo CSV: {e}")
     
print('Datos del fichero CSV')       
csv_handler = CSVFileHandler()
file_path = 'libros_unamuno.csv'
contenido_csv = csv_handler.read_csv(file_path)
print(contenido_csv, 'libreria_origen: Miguel de Unamuno')


json_handler.write_json('invertario_final.json')



# Inserción de Json en la base de datos
# try: 
#     if conexion is not None:
#         cursor = conexion.cursor()
#         print("Iniciando transacción...")
#         sql_insert = """
#             INSERT INTO Libros (titulo, autor, genero, año_publicacion, 'libreria_origen')
#             VALUES (%s, %s, %s, %s, %s)
#         """
#         datos_json = json_handler.read_json('libros_machado.json')
#         cursor.execute(sql_insert, datos_json)
#         conexion.commit()
#         print("Transacción exitosa: Registro insertado correctamente.")
#          # Mostrar los datos de la tabla
#         print("Tabla creada con exito")
#         cursor.execute("SELECT * FROM Libros")
#         for fila in cursor.fetchall():
#             print(fila)
# except MySQLError as e:
#     print(f"Error en la transacción: {e}") 
#     if conexion:
#         conexion.rollback()
#         print("Se realizó rollback.")
# finally:
#     if conexion and conexion is not None:
#         cursor.close()
#         conexion.close()
#         print("Conexión cerrada.")