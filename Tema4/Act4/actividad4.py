from ZODB import DB, FileStorage
from persistent import Persistent
import ZODB
import transaction
# Clase EdificiosHistorico
class EdificiosHistoricos(Persistent):
    def __init__(self, nombre, ubicacion, año, estilo):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.año = año
        self.estilo = estilo
# Conectar a la base de datos ZODB
storage = FileStorage.FileStorage('1dam.fs')
db = DB(storage)
connection = db.open()
root = connection.root()
# Función para gestionar la inserción de varios edificios con transacción
def agregar_edificios():
    try:
        print("Iniciando la transacción para agregar edificios...")
        # Verificar y crear 'edificios' en root si no existe
        if 'edificios' not in root:
            root['edificios'] = {} # Inicializar una colección de edificios si no existe
            transaction.commit() # Confirmar la creación en la base de datos
        # Crear y añadir nuevos edificios
        edificio1 = EdificiosHistoricos('Catedral de Santiago', 'España', '20/03/1812', 'Barroco')
        edificio2 = EdificiosHistoricos('Coliseo Romano', 'Roma', '18/09/1520', 'Romanico')
        edificio3 = EdificiosHistoricos('Piramides', 'Egipto', '29/10/1202', 'Barroco') 
        # Añadir edificios a la colección en la raíz de ZODB
        root['edificios']["Catedral de Santiago"] = edificio1
        root['edificios']["Coliseo Romano"] = edificio2
        root['edificios']["Piramides"] = edificio3
        # Confirmar la transacción
        transaction.commit()
        print("Transacción completada: Edificios añadidos correctamente.")
        # Mostrar datos
        for nombre, edificio in root['edificios'].items():
            print(f"Nombre: {edificio.nombre}, Ubicación: {edificio.ubicacion}, Año Construcción: {edificio.año}, Estilo: {edificio.estilo}")
    except Exception as e:
        # Si ocurre un error, revertimos la transacción
        transaction.abort()
        print(f"Error durante la transacción: {e}. Transacción revertida.")
        # Llamar a la función para añadir herramientas
agregar_edificios()
# Cerrar la conexión a la base de datos ZODB
connection.close()
db.close()