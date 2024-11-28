import ZODB, ZODB.FileStorage, transaction
from persistent import Persistent

from peewee import MySQLDatabase
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
class Libros(Model):
    id = int()
    titulo = CharField(100)
    autor = CharField(100)
    anio_publicacion = int()
    genero = CharField(50)
    class Meta:
        database = db # Base de datos
        table_name = 'Libros' # Nombre de la tabla en la base de datos
        
def tabla_existe(nombre_tabla):
    consulta = "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %s AND table_name = %s"
    cursor = db.execute_sql(consulta, ('1dam', nombre_tabla))
    resultado = cursor.fetchone()
    return resultado[0] > 0
# Eliminamos la tabla si ya existe para empezar a trabajar desde cero
if tabla_existe(Libros._meta.table_name):
    print(f"La tabla '{Libros._meta.table_name}' existe.")
    db.drop_tables([Libros], cascade=True)
    print(f"Tabla '{Libros._meta.table_name}' eliminada con éxito.")
else:
    print(f"La tabla '{Libros._meta.table_name}' no existe.")

# Crear la tabla si no existe
db.create_tables([Libros])
print("Tabla 'Libros' creada.")

# Insertar varios libros
Libros.create(titulo= 'Cien años de soledad', autor= 'Gabriel García Márquez', anio_publicacion= 1967, genero= 'Novela')
Libros.create(titulo= 'Don Quijote de la Mancha', autor= 'Miguel de Cervantes', anio_publicacion= 1605, genero= 'Novela')
Libros.create(titulo= 'El Principito', autor= 'Antoine de Saint-Exupéry', anio_publicacion= 1943, genero= 'Infantil')
Libros.create(titulo= 'Crónica de una muerte anunciada', autor= 'Gabriel García Márquez', anio_publicacion= 1981, genero= 'Novela')
Libros.create(titulo= '1984', autor= 'George Orwell', anio_publicacion= 1949, genero= 'Distopía')
print("Libros insertados correctamente en la base de datos.")


# Definir clase Prestamos
class Prestamos(Persistent):
    def __init__(self, libro_id, nombre_usuario, fecha_prestamo, fecha_devolucion):
        self.libros_id = libro_id
        self.nombre_usuario = nombre_usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

# Establecer conexión a la base de datos ZODB
storage = ZODB.FileStorage.FileStorage('1dam.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

# Almacenar prestamos
root['prestamo1'] = Libros(1, 'Juan Perez', '2023-10-01', '2023-11-01')
root['prestamo2'] = Libros(2, 'Ana Lopez', '2023-09-15', '2023-10-15')
root['prestamo3'] = Libros(4, 'Maria Gomez', '2023-09-20', '2023-10-20')
print("Préstamos almacenados correctamente en ZOBD")
transaction.commit()

def buscar_prestamos_por_genero(genero_elegido):
    if Libros.genero == genero_elegido:
        print("Préstamos de libros del género", genero_elegido)
        novelas = Libros.select().where(Libros.genero == genero_elegido)
        for novela in novelas:
            print(f'Libro: {novela.titulo}')
    else:
        print("El género elegido no se encuentra registrado.")
    
        
    #   for prestamo in root.items():
    #      if novela.id == :
    #print(f"Libro: {Libros.titulo}, Usuario: {Prestamos.nombre_usuario}, Fecha Préstamo: {Prestamos.fecha_prestamo}, Fecha Devolución: {Prestamos.fecha_devolucion}")
    
    
buscar_prestamos_por_genero('Novela')