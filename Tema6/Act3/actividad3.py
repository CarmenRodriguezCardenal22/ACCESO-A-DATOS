import logging
from peewee import Model, CharField, ForeignKeyField, MySQLDatabase, DoesNotExist
# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("databasemanager_orm.log"),
        logging.StreamHandler()
    ]
)
# Configuración de la base de datos MySQL
db = MySQLDatabase(
    "1dam",  # Nombre de la base de datos
    user="usuario",  # Usuario de MySQL
    password="usuario",  # Contraseña de MySQL
    host="localhost",  # Host
    port=3306  # Puerto por defecto de MySQL
)
# Modelos de la base de datos
class Proveedor(Model):
    nombre = CharField(unique=True)
    direccion = CharField()
    class Meta:
        database = db

class Herramienta(Model):
    nombre = CharField()
    tipo = CharField()
    marca = CharField()
    uso = CharField()
    material = CharField()
    proveedor = ForeignKeyField(Proveedor, backref='herramientas')
    class Meta:
        database = db

# Componente DatabaseManagerORM
class DatabaseManagerORM:
    def __init__(self):
        self.db = db
    def conectar(self):
        """Conecta la base de datos y crea las tablas."""
        self.db.connect()
        self.db.create_tables([Proveedor, Herramienta])
        logging.info("Conexión establecida y tablas creadas.")
    def desconectar(self):
        """Cierra la conexión a la base de datos."""
        if not self.db.is_closed():
            self.db.close()
            logging.info("Conexión cerrada.")
    def iniciar_transaccion(self):
        """Inicia una transacción."""
        self.db.begin()
        logging.info("Transacción iniciada.")
    def confirmar_transaccion(self):
        """Confirma (commit) una transacción."""
        self.db.commit()
        logging.info("Transacción confirmada.")
    def revertir_transaccion(self):
        """Revierte (rollback) una transacción."""
        self.db.rollback()
        logging.info("Transacción revertida.")
    def crear_proveedor(self, nombre, direccion):
        """Inserta un nuevo proveedor."""
        proveedor = Proveedor.create(nombre=nombre, direccion=direccion)
        logging.info(f"Proveedor creado: {proveedor.nombre} - {proveedor.direccion}")
        return proveedor
    def crear_herramienta(self, nombre, tipo, marca, uso, material, proveedor_nombre):
        """Inserta una nueva herramienta."""
        proveedor = Proveedor.get_or_none(Proveedor.nombre == proveedor_nombre)
        if not proveedor:
            raise ValueError(f"No existe un proveedor con el nombre {proveedor_nombre}")
        herramienta = Herramienta.create(
            nombre=nombre, tipo=tipo, marca=marca, uso=uso, material=material, proveedor=proveedor
        )
        logging.info(f"Herramienta creada: {herramienta.nombre} - {herramienta.tipo}")
        return herramienta
    def leer_herramientas(self):
        """Lee todas las herramientas."""
        herramientas = Herramienta.select()
        logging.info("Leyendo herramientas:")
        for herramienta in herramientas:
            logging.info(f"{herramienta.nombre} - {herramienta.tipo} ({herramienta.proveedor.nombre})")
        return herramientas
    def actualizar_herramienta(self, nombre, tipo, marca, uso, material):
        """Actualizar una herramienta en la base de datos."""
        try:
            herramienta = Herramienta.get(Herramienta.nombre == nombre)
            herramienta.tipo = tipo
            herramienta.marca = marca
            herramienta.uso = uso
            herramienta.material = material
            herramienta.save()
            logging.info(f"Herramienta {nombre} actualizada exitosamente.")
        except DoesNotExist:
            logging.error(f"No se encontró la herramienta con nombre {nombre}.")
    def actualizar_proveedor(self, nombre, direccion):
        """Actualizar un proveedor en la base de datos."""
        try:
            proveedor = Proveedor.get(Proveedor.nombre == nombre)
            proveedor.direccion = direccion
            proveedor.save()
            logging.info(f"Proveedor {nombre} actualizado exitosamente.")
        except DoesNotExist:
            logging.error(f"No se encontró el proveedor con nombre {nombre}.")
    def eliminar_herramienta(self, nombre):
        """Eliminar una herramienta de la base de datos."""
        try:
            herramienta = Herramienta.get(Herramienta.nombre == nombre)
            herramienta.delete_instance()
            logging.info(f"Herramienta {nombre} eliminada exitosamente.")
        except DoesNotExist:
            logging.error(f"No se encontró la herramienta con nombre {nombre}.")
    def eliminar_proveedor(self, nombre):
        """Eliminar un proveedor de la base de datos."""
        try:
            proveedor = Proveedor.get(Proveedor.nombre == nombre)
            proveedor.delete_instance()
            logging.info(f"Proveedor {nombre} eliminado exitosamente.")
        except DoesNotExist:
            logging.error(f"No se encontró el proveedor con nombre {nombre}.")
    def consultar_herramientas_proveedor(self, proveedor_nombre):
        """Consulta herramientas asociadas a un proveedor."""
        proveedor = Proveedor.get_or_none(Proveedor.nombre == proveedor_nombre)
        if not proveedor:
            logging.error(f"No existe un proveedor con el nombre {proveedor_nombre}")
            return
        herramientas = Herramienta.select().where(Herramienta.proveedor == proveedor)
        logging.info(f"Herramientas asociadas a {proveedor.nombre}:")
        for herramienta in herramientas:
            logging.info(f"{herramienta.nombre} - {herramienta.tipo}")


# Ejemplo de uso
database = DatabaseManagerORM()
database.conectar()
#database.eliminar_herramienta("Martillo")
#database.eliminar_proveedor("ProveedorA")

print("\nGestión de Proveedores:")
database.iniciar_transaccion()
database.crear_proveedor("ProveedorA", "123-456-789")
database.crear_proveedor("ProveedorB", "987-654-321")
database.confirmar_transaccion()
print("\nCambio de dato por mi DNI 30284233H al ProveedorA:")
database.iniciar_transaccion()
database.actualizar_proveedor("ProveedorA", "30284233")
database.confirmar_transaccion()
print("Eliminar ProveedorB:")
database.iniciar_transaccion()
database.eliminar_proveedor("ProveedorB")
database.confirmar_transaccion()
print("\nGestión de Herramientas:")
database.iniciar_transaccion()
database.crear_herramienta("Martillo", "Manual", "Facom", "Percusión", "Acero", "ProveedorA")
database.crear_herramienta("Taladro", "Electrico", "Facom", "Percusión", "Acero", "ProveedorA")
database.confirmar_transaccion()
print("\nHerramientas asociadas al ProveedorA:")
database.consultar_herramientas_proveedor("ProveedorA")
database.iniciar_transaccion()
print("\nActualizar herramienta Martillo a tipo reforzado:")
database.actualizar_herramienta("Martillo", "Reforzado", "Facom", "Percusion", "Acero")
database.confirmar_transaccion()
print("\nEliminar herramienta Taladro:")
database.iniciar_transaccion()
database.eliminar_herramienta("Taladro")
database.confirmar_transaccion()
database.desconectar()

