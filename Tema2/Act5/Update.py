import pymysql
conexion = pymysql.connect(
    host="localhost", 
    user="usuario", 
    password="usuario", 
    db="1dam"
)
cursor = conexion.cursor()
cursor.execute(
    "UPDATE EdificiosHistoricos SET añoContruccion = %s WHERE nombre = %s", ('20/06/1840', 'Torre del Oro')
)

conexion.commit()
print('Actualización existosa')
conexion.close()