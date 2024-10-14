import pymysql
conexion = pymysql.connect(
    host="localhost", 
    user="usuario", 
    password="usuario", 
    db="1dam"
)
cursor = conexion.cursor()
cursor.execute("""
create table if not exists Autores(
nombre varchar(50) PRIMARY KEY,
fechaNacimiento varchar(50),
edificio varchar(50));
""")
cursor.execute("""
ALTER TABLE Autores
ADD CONSTRAINT edificio
FOREIGN KEY (edificio) REFERENCES EdificiosHistoricos(nombre);
""")

conexion.commit()
print('Creación de la tabla Autores existosa')
print('Creación de la clave foránea existosa')
conexion.close()