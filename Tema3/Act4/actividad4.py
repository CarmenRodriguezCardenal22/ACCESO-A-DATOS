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
        
        
# Recuperar todos los edificios de la base de datos
print('Registros iniciales')
edificios = EdificiosHistoricos.select()
for edificio in edificios:
    print(f"Nombre: {edificio.nombre}, Ubicacion: {edificio.ubicacion}, AñoConstruccion: {edificio.añoConstruccion}, EstiloArquitectonico: {edificio.estiloArquitectonico}")
        
print('\nTarea 1')

# Recuperar todos los edificios de la base de datos con estilo 'Barroco'
print('Registros con estilo Barroco')
edificios = EdificiosHistoricos.select().where(EdificiosHistoricos.estiloArquitectonico == 'Barroco')
for edificio in edificios:
    print(f"Nombre: {edificio.nombre}, Ubicacion: {edificio.ubicacion}, AñoConstruccion: {edificio.añoConstruccion}, EstiloArquitectonico: {edificio.estiloArquitectonico}")
  
print('\nTarea 2')

# Recuperar todos los edificios de la base de datos
print('Registros exisentes')
edificios = EdificiosHistoricos.select()
for edificio in edificios:
    print(f"Nombre: {edificio.nombre}, Ubicacion: {edificio.ubicacion}, AñoConstruccion: {edificio.añoConstruccion}, EstiloArquitectonico: {edificio.estiloArquitectonico}")
    
print("\nEdificiosHistoricos 'Torre Eiffel' y 'Renacentista' eliminada.")
# Eliminar un edificio específico por nombre
try:
    # Iniciar una transacción utilizando db.atomic()
    with db.atomic():
        torreEiffel = EdificiosHistoricos.get((EdificiosHistoricos.nombre == 'Torre Eiffel') & (EdificiosHistoricos.estiloArquitectonico == 'Renacentista'))
        torreEiffel.delete_instance()
except IntegrityError as e:
    print(f"Error al insertar herramientas: {e}")
# Recupera todos los registros después de la eliminación
edificios = EdificiosHistoricos.select()
for edificio in edificios:
    print(f"Nombre: {edificio.nombre}, Ubicacion: {edificio.ubicacion}, AñoConstruccion: {edificio.añoConstruccion}, EstiloArquitectonico: {edificio.estiloArquitectonico}")

  
print('\nTarea 3')

# Recuperar todos los edificios de la base de datos
print('Registros existentes')
edificios = EdificiosHistoricos.select()
for edificio in edificios:
    print(f"Nombre: {edificio.nombre}, Ubicacion: {edificio.ubicacion}, AñoConstruccion: {edificio.añoConstruccion}, EstiloArquitectonico: {edificio.estiloArquitectonico}")
    
# Eliminar todos los edificios con el nombre 'Torre Eiffel' y estilo 'Renacentista'
try:
    # Iniciar una transacción utilizando db.atomic()
    with db.atomic():
        EdificiosHistoricos.delete().where(EdificiosHistoricos.estiloArquitectonico == 'Barroco').execute()
except IntegrityError as e:
    print(f"Error al insertar herramientas: {e}")
print("\nEdificiosHistoricos del estilo 'Barroco' eliminados.")
# Recupera todos los registros después de la eliminación
edificios = EdificiosHistoricos.select()
for edificio in edificios:
    print(f"Nombre: {edificio.nombre}, Ubicacion: {edificio.ubicacion}, AñoConstruccion: {edificio.añoConstruccion}, EstiloArquitectonico: {edificio.estiloArquitectonico}")