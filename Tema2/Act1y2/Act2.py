import pymysql
conexion = pymysql.connect(
    host="localhost", 
    user="usuario", 
    password="usuario", 
    database="1dam"
)
cursor = conexion.cursor()
cursor.execute("""
create table if not exists EdificiosHistoricos(
nombre varchar(50) PRIMARY KEY,
ubicacion varchar(50),
añoContruccion varchar(50),
estiloArquitectonico varchar(50));
""")
# Insertar datos en la tabla
cursor.execute(
"INSERT into EdificiosHistoricos values
('Torre del Oro','Sevilla','10/01/1960','Barroco'),
)
# Confirmar los cambios
conexion.commit()
# Realizar una consulta para recuperar los datos
cursor.execute("SELECT * FROM EdificiosHistoricos")
# Imprimir todos los registros
for fila in cursor.fetchall():
print(fila)
# Cerrar la conexión
conexion.close()