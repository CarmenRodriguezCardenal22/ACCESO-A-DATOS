import pymysql
conexion = pymysql.connect(
    host="localhost", 
    user="usuario", 
    password="usuario", 
    db="1dam"
)
cursor = conexion.cursor()

cursor.execute(
   "DELETE FROM EdificiosHistoricos WHERE nombre = %s", ('Torre del Oro',)
)

conexion.commit()
print('Eliminación existosa')
conexion.close()