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
    # Consulta para filtrar los documentos
    consulta = {"estiloArquitectonico": "Barroco"}
    # Proyección para excluir ciertos campos
    # Solo incluir 'nombre' y 'estiloArquitectonico', y excluir 'ubicacion' y 'añoContruccion'
    proyeccion = {"nombre": 1, "estiloArquitectonico": 1, "_id": 0}  # Excluye automáticamente '_id'
    # Realizar la consulta con proyección
    resultados = coleccion.find(consulta, proyeccion)
    # Imprimir los resultados
    for resultado in resultados:
        print(resultado)
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

