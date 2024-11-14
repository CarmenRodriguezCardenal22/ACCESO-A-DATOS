from pymongo import MongoClient, errors
# Datos de conexión
usuario = "usuario"
clave = "usuario"
base_datos = "1dam"
host = "localhost"
puerto = 27017
try:
    # Intentar conectarse al servidor MongoDB
    client = MongoClient(f"mongodb://{usuario}:{clave}@{host}:{puerto}/{base_datos}",serverSelectionTimeoutMS=5000)
    # Seleccionar la base de datos
    db = client[base_datos]
    # Acceder a la colección 'EdificiosHistoricos'
    coleccion = db["EdificiosHistoricos"]
    # Obtener los primeros 2 documentos (limit)
    usuarios = coleccion.find().limit(2)
    print("Primeros 3 documentos:")
    for usuario in usuarios:
        print(usuario)
    # Ordenar los documentos por el campo "edad" en orden descendente (sort)
    usuarios = coleccion.find().sort("nombre", 1)  
    print("\nDocumentos ordenados por 'edad' de mayor a menor:")
    for usuario in usuarios:
        print(usuario)
except errors.ServerSelectionTimeoutError as err:
    print(f"No se pudo conectar a MongoDB: {err}")
except errors.OperationFailure as err:
    print(f"Fallo en la autenticación o permisos insuficientes: {err}")
except Exception as err:
    print(f"Ocurrió un error inesperado: {err}")
finally:
    # Cerrar la conexión si se estableció correctamente
    if 'client' in locals():
        client.close()
        print("Conexión cerrada.")
