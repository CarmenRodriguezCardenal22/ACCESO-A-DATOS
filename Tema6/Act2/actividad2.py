import logging
import mysql.connector
from mysql.connector import Error
# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("databasemanager.log"), # Logs guardados en un archivo
        logging.StreamHandler(), # Logs también en consola
    ]
)
class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    def conectar(self):
        """Conectar a la base de datos MySQL"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                logging.info("Conexión exitosa a la base de datos.")
        except Error as e:
            logging.error(f"Error al conectar a la base de datos: {e}")
    def desconectar(self):
        """Cerrar la conexión a la base de datos"""
        if self.connection.is_connected():
            self.connection.close()
            logging.info("Conexión cerrada.")
    def crear_edificios(self, nombre, ubicacion, añoConstruccion, estiloArquitectonico):
        """Insertar una nueva herramienta en la base de datos"""
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO EdificiosHistoricos (nombre, ubicacion, añoConstruccion, estiloArquitectonico)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (nombre, ubicacion, ubicacion, añoConstruccion, estiloArquitectonico))
            logging.info(f"Edificio '{nombre}' insertado exitosamente.")
        except Error as e:
            logging.error(f"Error al insertar el edificio '{nombre}': {e}")
    def leer_edificios(self):
        """Leer todos los edificios de la base de datos"""
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM EdificiosHistoricos")
            edificios = cursor.fetchall()
            logging.info("Edificios recuperados:")
            for edificio in edificios:
                logging.info(edificio)
            return edificios
        except Error as e:
            logging.error(f"Error al leer los edificios: {e}")
            return None
    def actualizar_edificios(self, id, nombre, ubicacion, añoConstruccion, estiloArquitectonico):
        """Actualizar un edificio en la base de datos"""
        try:
            cursor = self.connection.cursor()
            query = """
                UPDATE EdificiosHistoricos
                SET nombre = %s, ubicacion = %s, añoConstruccion = %s, estiloArquitectonico = %s
                WHERE id = %s
            """
            cursor.execute(query, (nombre, ubicacion, añoConstruccion, estiloArquitectonico, id))
            self.connection.commit()
            logging.info(f"Edificio con ID {id} actualizado exitosamente.")
        except Error as e:
            logging.error(f"Error al actualizar el edificio con ID {id}: {e}")
    def eliminar_edificios(self, id):
        """Eliminar un edificio de la base de datos"""
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM EdificiosHistoricos WHERE id = %s"
            cursor.execute(query, (id,))
            self.connection.commit()
            logging.info(f"Edificio con ID {id} eliminado exitosamente.")
        except Error as e:
            logging.error(f"Error al eliminar el edificio con ID {id}: {e}")
    def iniciar_transaccion(self):
        """Iniciar una transacción"""
        try:
            if self.connection.is_connected():
                self.connection.start_transaction()
                logging.info("Transacción iniciada.")
        except Error as e:
            logging.error(f"Error al iniciar la transacción: {e}")
    def confirmar_transaccion(self):
        """Confirmar (commit) una transacción"""
        try:
            if self.connection.is_connected():
                self.connection.commit()
                logging.info("Transacción confirmada.")
        except Error as e:
            logging.error(f"Error al confirmar la transacción: {e}")
    def revertir_transaccion(self):
        """Revertir (rollback) una transacción"""
        try:
            if self.connection.is_connected():
                self.connection.rollback()
                logging.info("Transacción revertida.")
        except Error as e:
            logging.error(f"Error al revertir la transacción: {e}")
# Ejemplo de uso del componente DatabaseManager
if __name__ == "__main__":
    db_manager = DatabaseManager("localhost", "usuario", "usuario", "1dam")
    db_manager.conectar()
    # Insertar un nuevo edificio
    db_manager.crear_edificios("Cristo Redentor", "Rio de Janeiro", "27/05/1352", "Renacentista")
    # Leer todos los edificio
    db_manager.leer_edificios()
    # Actualizar un edificio
    db_manager.actualizar_edificios(1, "Cristo Redentor", "Rio de Janeiro", "27/05/1352", "Gótico")
    # Eliminar un edificio
    db_manager.eliminar_edificios(1)
    # Gestionar transacciones
    db_manager.iniciar_transaccion()
    db_manager.crear_edificios("Piramides", "Egipto", "10/01/1502", "Egipto")
    db_manager.revertir_transaccion() # No se guardará la inserción
    db_manager.desconectar()