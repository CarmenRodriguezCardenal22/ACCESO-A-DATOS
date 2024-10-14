import pymysql
conexion = pymysql.connect(
    host="localhost", 
    user="usuario", 
    password="usuario", 
    db="1dam"
)
cursor1 = conexion.cursor()
cursor2 = conexion.cursor()
print('Primera lectura')
cursor1.execute("SELECT * FROM EdificiosHistoricos")
for i in range(1,6):
    fila = cursor1.fetchone()
    print(fila)
print('Segunda lectura')
cursor2.execute("SELECT * FROM EdificiosHistoricos")
for i in range(1,6):
    fila = cursor2.fetchone()
    print(fila)
cursor1.close()
cursor2.close()
conexion.commit()
conexion.close()