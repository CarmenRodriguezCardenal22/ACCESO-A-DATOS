from peewee import MySQLDatabase
from peewee import IntegrityError
# Configurar la base de datos
db = MySQLDatabase(
    '1dam', # Nombre de la base de datos
    user='usuario', # Usuario de MySQL
    password='usuario', # Contraseña de MySQL
    host='localhost', # Host
    port=3306 # Puerto por defecto de MySQL
)
# Conectar a la base de datos
db.connect()
print("Conexión exitosa a la base de datos.")

from peewee import Model, CharField
# Definir el mapeo de la tabla EdificiosHistoricos
class EdificiosHistoricos(Model):
    nombre = CharField()
    ubicacion = CharField()
    añoConstruccion = CharField()
    estiloArquitectonico = CharField()
    class Meta:
        database = db # Base de datos
        table_name = 'EdificiosHistoricos' # Nombre de la tabla en la base de datos
        
def tabla_existe(nombre_tabla):
    consulta = "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %s AND table_name = %s"
    cursor = db.execute_sql(consulta, ('1dam', nombre_tabla))
    resultado = cursor.fetchone()
    return resultado[0] > 0
# Eliminamos la tabla si ya existe para empezar a trabajar desde cero
if tabla_existe(EdificiosHistoricos._meta.table_name):
    print(f"La tabla '{EdificiosHistoricos._meta.table_name}' existe.")
    db.drop_tables([EdificiosHistoricos], cascade=True)
    print(f"Tabla '{EdificiosHistoricos._meta.table_name}' eliminada con éxito.")
else:
    print(f"La tabla '{EdificiosHistoricos._meta.table_name}' no existe.")

# Crear la tabla si no existe
db.create_tables([EdificiosHistoricos])
print("Tabla 'EdificiosHistoricos' creada.")
try:
    # Iniciar una transacción utilizando db.atomic()
    with db.atomic():
        # Insertar varios edificios
        EdificiosHistoricos.create(nombre='Estatua de la Libertad',ubicacion='New York',añoConstruccion='14/10/1886',estiloArquitectonico='Barroco')
        EdificiosHistoricos.create(nombre='Giralda',ubicacion='España',añoConstruccion='05/03/1979',estiloArquitectonico='Barroco')
        EdificiosHistoricos.create(nombre='Taj Majal', ubicacion='India', añoConstruccion='06/06/1990', estiloArquitectonico='Moderno')
        EdificiosHistoricos.create(nombre='Torre de Pisa', ubicacion='Roma', añoConstruccion='15/12/1214', estiloArquitectonico='Renacentista')
        EdificiosHistoricos.create(nombre='Torre Eiffel', ubicacion='París', añoConstruccion='20/09/1650', estiloArquitectonico='Renacentista')

        print("EdificiosHistoricos insertadas en la base de datos.")
except IntegrityError as e:
    print(f"Error al insertar herramientas: {e}")