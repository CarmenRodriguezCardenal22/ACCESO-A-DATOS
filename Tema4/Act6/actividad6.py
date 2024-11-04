from persistent import Persistent
import ZODB, ZODB.FileStorage
import transaction 
import copy
# Clases para EdificiosHistoicos y Arquitectos
class EdificiosHistoricos(Persistent):
    def __init__(self, nombre, ubicacion, añoConstruccion, estiloArquitectonico, id_arquitecto):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.añoConstruccion = añoConstruccion
        self.estiloArquitectonico = estiloArquitectonico
        self.id_arquitecto = id_arquitecto # ID del arquitecto
class Arquitectos(Persistent):
    def __init__(self, id, nombre, añoNacimiento, paisOrigen):
        self.id =id
        self.nombre = nombre
        self.añoNacimiento = añoNacimiento
        self.paisOrigen = paisOrigen
        
storage = ZODB.FileStorage.FileStorage('1dam.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

# Verificar y crear colecciones si no existen
if 'edificios' not in root:
    root['edificios'] = {}
if 'arquitectos' not in root:
    root['arquitectos'] = {}
# Insertar datos en Arquitectos
root['arquitectos']['Arquitecto1'] = Arquitectos("1", "Ahmad Ben Baso", "1645", "Marruecos")
root['arquitectos']['Arquitecto2'] = Arquitectos("2", "Erich Honecker", "1230", "Alemania")
# Insertar datos en Edificios, incluyendo id_arquitecto
root['edificios']['Edificio1'] = EdificiosHistoricos("Giralda", "España", "16/06/1650", "Gótico", "1")
root['edificios']['Edificio2'] = EdificiosHistoricos("Coliseo Romano","Roma", "24/01/1520", "Renacentista", "2")
root['edificios']['Edificio3'] = EdificiosHistoricos("Muro de Berlín", "Alemania", "01/10/1760", "Barroco", "2")
transaction.commit()


edificio_original = root['edificios']['Edificio1']
edificio_copia = copy.deepcopy(edificio_original)
    
edificio_copia = copy.deepcopy(edificio_original)
edificio_copia.estiloArquitectonico = "Moderno"
print("Original: ", edificio_original.estiloArquitectonico)
print("Copia: ", edificio_copia.estiloArquitectonico)
