import logging
import transaction
from ZODB import DB, FileStorage
from persistent import Persistent

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("databasemanager_object.log"),  # Logs guardados en un archivo
        logging.StreamHandler(),  # Logs también en consola
    ],
)

class Edificio(Persistent):
    """Clase que representa un edificio."""
    def __init__(self, nombre, ubicacion, año_construccion, estilo_arquitectonico):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.año_construccion = año_construccion
        self.estilo_arquitectonico = estilo_arquitectonico


class DatabaseManagerObject:
    """Componente para gestionar bases de datos orientadas a objetos con ZODB."""
    def __init__(self, filepath="edificios.fs"):
        self.filepath = filepath
        self.db = None
        self.connection = None
        self.root = None
        self.transaccion_iniciada = False

    def conectar(self):
        """Conecta a la base de datos ZODB."""
        try:
            storage = FileStorage.FileStorage(self.filepath)
            self.db = DB(storage)
            self.connection = self.db.open()
            self.root = self.connection.root()
            if "edificios" not in self.root:
                self.root["edificios"] = {}
            transaction.commit()
            logging.info("Conexión establecida con ZODB.")
        except Exception as e:
            logging.error(f"Error al conectar a ZODB: {e}")

    def desconectar(self):
        """Cierra la conexión a la base de datos."""
        try:
            if self.connection:
                self.connection.close()
            self.db.close()
            logging.info("Conexión a ZODB cerrada.")
        except Exception as e:
            logging.error(f"Error al cerrar la conexión a ZODB: {e}")

    def iniciar_transaccion(self):
        """Inicia una transacción."""
        try:
            transaction.begin()
            self.transaccion_iniciada = True
            logging.info("Transacción iniciada.")
        except Exception as e:
            logging.error(f"Error al iniciar la transacción: {e}")

    def confirmar_transaccion(self):
        """Confirma la transacción."""
        if self.transaccion_iniciada:
            try:
                transaction.commit()
                self.transaccion_iniciada = False
                logging.info("Transacción confirmada.")
            except Exception as e:
                logging.error(f"Error al confirmar la transacción: {e}")

    def revertir_transaccion(self):
        """Revierte la transacción."""
        if self.transaccion_iniciada:
            try:
                transaction.abort()
                self.transaccion_iniciada = False
                logging.info("Transacción revertida.")
            except Exception as e:
                logging.error(f"Error al revertir la transacción: {e}")

    def crear_edificio(self, id, nombre, ubicacion, año_construccion, estilo_arquitectonico):
        """Crea y almacena un nuevo edificio."""
        try:
            if id in self.root["edificios"]:
                raise ValueError(f"Ya existe un edificio con ID {id}.")
            self.root["edificios"][id] = Edificio(nombre, ubicacion, año_construccion, estilo_arquitectonico)
            logging.info(f"Edificio con ID {id} creado exitosamente.")
        except Exception as e:
            logging.error(f"Error al crear el edificio con ID {id}: {e}")

    def leer_edificios(self):
        """Lee y muestra todos los edificios almacenados."""
        try:
            edificios = self.root["edificios"]
            for id, edificio in edificios.items():
                logging.info(
                    f"ID: {id}, Nombre: {edificio.nombre}, Ubicación: {edificio.ubicacion}, "
                    f"Año de Construcción: {edificio.año_construccion}, Estilo Arquitectónico: {edificio.estilo_arquitectonico}"
                )
            return edificios
        except Exception as e:
            logging.error(f"Error al leer los edificios: {e}")

    def actualizar_edificio(self, id, nombre, ubicacion, año_construccion, estilo_arquitectonico):
        """Actualiza los atributos de un edificio."""
        try:
            edificio = self.root["edificios"].get(id)
            if not edificio:
                raise ValueError(f"No existe un edificio con ID {id}.")
            edificio.nombre = nombre
            edificio.ubicacion = ubicacion
            edificio.año_construccion = año_construccion
            edificio.estilo_arquitectonico = estilo_arquitectonico
            logging.info(f"Edificio con ID {id} actualizado exitosamente.")
        except Exception as e:
            logging.error(f"Error al actualizar el edificio con ID {id}: {e}")

    def eliminar_edificio(self, id):
        """Elimina un edificio por su ID."""
        try:
            if id not in self.root["edificios"]:
                raise ValueError(f"No existe un edificio con ID {id}.")
            del self.root["edificios"][id]
            logging.info(f"Edificio con ID {id} eliminado exitosamente.")
        except Exception as e:
            logging.error(f"Error al eliminar el edificio con ID {id}: {e}")


if __name__ == "__main__":
    manager = DatabaseManagerObject()
    manager.conectar()
    
    # Crear edificios con transacción
    manager.iniciar_transaccion()
    manager.crear_edificio(1, "Torre Eiffel", "París", "12/11/1889", "Arquitectura de Hierro")
    manager.crear_edificio(2, "Empire State", "Nueva York", "22/05/1931", "Art Deco")
    manager.crear_edificio(3, "Louvre", "Paris", "01/06/1520", "Moderno")
    manager.confirmar_transaccion()
    
    # Leer edificios
    manager.leer_edificios()

    # Crear edificio con ID ya insertado 
    try:
        manager.crear_edificio(3, "Sagrada Familia", "España", "20/02/1230", "Gótico")
    except Exception as e:
        logging.error(f"Error general: {e}")
        manager.revertir_transaccion()
    
    # Leer edificios
    manager.leer_edificios()
    
    # Actualizar un edificio con transacción
    manager.iniciar_transaccion()
    manager.actualizar_edificio(1, "Torre Eiffel", "París", "11/12/1889", "Arquitectura Moderna")
    manager.confirmar_transaccion()
    
    # Leer edificios
    manager.leer_edificios()
    
    # Eliminar un edificio con transacción con ID no registrado
    try:
        manager.eliminar_edificio(7)
    except ValueError as e:
        logging.error(f"Error general: {e}")
        manager.revertir_transaccion()
        
    # Leer edificios nuevamente
    manager.leer_edificios()

    manager.desconectar()
