import ZODB, ZODB.FileStorage, transaction
from persistent import Persistent

# Definir clase Edificios
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

# Almacenar una edificios
root['edificios'] = ""
root['edificios1'] = EdificiosHistoricos('Catedral de Santiago', 'España', '20/03/1812', 'Barroco')
root['edificios2'] = EdificiosHistoricos('Coliseo Romano', 'Roma', '18/09/1520', 'Romanico')
root['edificios3'] = EdificiosHistoricos('Piramides', 'Egipto', '29/10/1202', 'Barroco')
transaction.commit()

# Filtrar edificios por tipo
estilo_deseado = "Barroco"
for clave, edificios in root.items():
    if hasattr(edificios, 'estilo') and edificios.estilo == estilo_deseado:
        print(f"Nombre: {edificios.nombre}, Ubicación: {edificios.ubicacion}, Año de Construcción: {edificios.año}, Estilo Arquitectónico: {edificios.estilo}")

# Cerrar la conexión
connection.close()
db.close()