import ZODB, ZODB.FileStorage, transaction
from persistent import Persistent
# Definir la clase Edificios
class EdificiosHistoricos(Persistent):
    def __init__(self, nombre, ubicacion, año, estilo):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.año = año
        self.estilo = estilo
# Establecer conexión a la base de datos ZODB
storage = ZODB.FileStorage.FileStorage('1dam.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()
# Recuperar y modificar un objeto
edificios = root.get('edificios3') # Recuperar los edificios almacenada con la clave 'piramides'
print('Antes de modificar:', edificios)
if edificios:
    print("Antes de la modificación:")
    print(f"Nombre: {edificios.nombre}, Estilo: {edificios.estilo}")
    # Modificar el atributo 'estilo'
    edificios.estilo = 'Egipcio'
    transaction.commit() # Confirmar los cambios en la base de datos
    print("Después de la modificación:")
    print(f"Nombre: {edificios.nombre}, Estilo: {edificios.estilo}")
else:
    print("El edificio no se encontró en la base de datos.")
# Cerrar la conexión
connection.close()
db.close()