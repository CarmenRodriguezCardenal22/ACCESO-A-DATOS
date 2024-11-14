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
    # Definir varios documentos de edificios 
    edificios = [
        {"nombre": "Coliseo Romano", "ubicacion": "Italia", "añoContruccion": "01/01/1414", "estiloArquitectonico": "Barroco"},
        {"nombre": "Sagrada Familia", "ubicacion": "España", "añoContruccion": "30/03/1190", "estiloArquitectonico": "Gótico"},
        {"nombre": "Big Ben", "ubicacion": "Inglaterra", "añoContruccion": "17/09/1365", "estiloArquitectonico": "Renacentista"}
    ]
    # Insertar múltiples documentos en la colección
    resultado = coleccion.insert_many(edificios)
    print("IDs de documentos insertados:", resultado.inserted_ids)
    # Actualizar un documento (cambiar el estilo arquitectónico del Coliseo Romano)
    resultado = coleccion.update_one(
        {"nombre": "Coliseo Romano"},  # Filtro para encontrar el documento
        {"$set": {"estiloArquitectonico": "Románico"}}  # Campos que deseas modificar
    )
    # Verificar si el documento fue actualizado
    if resultado.modified_count >= 0:
        print("Documento modificado con éxito.")
    else:
        print("No se encontró el documento o no hubo cambios.")
    # Eliminar un solo documento (eliminar el Big Ben)
    resultado = coleccion.delete_one({"nombre": "Big Ben"})
    # Verificar si el documento fue eliminado
    if resultado.deleted_count > 0:
        print("Documento eliminado con éxito.")
    else:
        print("No se encontró el documento para eliminar.")  
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
