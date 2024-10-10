import pymysql

conexion = pymysql.connect(
    host="localhost", 
    user="usuario", 
    password="usuario", 
    db="1dam"
)

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS EdificiosHistoricos(
    nombre VARCHAR(50) PRIMARY KEY,
    ubicacion VARCHAR(50),
    añoContruccion VARCHAR(50),
    estiloArquitectonico VARCHAR(50)
);
""")

cursor.execute(
    "INSERT INTO EdificiosHistoricos (nombre, ubicacion, añoContruccion, estiloArquitectonico) VALUES (%s, %s, %s, %s)",
    ('Torre del Oro', 'Sevilla', '10/03/1960', 'Barroco')
)

conexion.commit()

cursor.execute("SELECT * FROM EdificiosHistoricos")
for fila in cursor.fetchall():
    print(fila)

conexion.close()
