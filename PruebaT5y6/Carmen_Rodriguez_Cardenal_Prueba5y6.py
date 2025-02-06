from pymongo import MongoClient, errors
# Datos de conexión
usuario = "usuario"
clave = "usuario"
base_datos = "test"
host = "localhost"
puerto = 27017
try:
    # Intentar conectarse al servidor MongoDB
    client = MongoClient(f"mongodb://{usuario}:{clave}@{host}:{puerto}/{base_datos}",serverSelectionTimeoutMS=5000)
    # Seleccionar la base de datos
    db = client[base_datos]
    # Acceder a la colección 'Productos'
    coleccion = db["Productos"]
    # Definir varios documentos de productos 
    productos = [
        {"nombre": "Drone Phantom X", "categoria": "Drones", "precio": 1200.50, "stock": 8},
        {"nombre": "Auriculares Sonic Boom", "categoria": "Auriculares", "precio": 299.99, "stock": 15},
        {"nombre": "Cámara Action Pro", "categoria": "Cámaras", "precio": 499.99, "stock": 10},
        {"nombre": "Asistente SmartBuddy", "categoria": "Asistentes Inteligentes", "precio": 199.99,"stock": 20},
        {"nombre": "Cargador Solar Ultra", "categoria": "Accesorios", "precio": 49.99, "stock": 3}
    ]
    # Insertar múltiples documentos en la colección
    resultado = coleccion.insert_many(productos)
    
    print('Objetos de la lista:')
    for producto in productos:
        print(producto["nombre"], producto["categoria"], producto["precio"], producto["stock"])
    
    # Realizar la consulta y ordenación
    print('\nObjetos con categoria "Auriculares"')
    consulta = {"categoria": "Auriculares"}
    usuarios = coleccion.find(consulta).sort("precio", -1)
    for usuario in usuarios:
        print(usuario["nombre"], usuario["precio"], usuario["stock"])
        
        
    # Actualizar registros
    print('\nRegistros antes de la actualización')
    for producto in productos:
        print(producto["nombre"], producto["categoria"], producto["precio"], producto["stock"])
    resultado = coleccion.update_one(
        {"nombre": "Drone Phantom X"},  # Filtro para encontrar el documento
        {"$set": {"precio": "1300"}}  # Campos que deseas modificar
    )
    # Verificar si el documento fue actualizado
    if resultado.modified_count >= 0:
        print("Documento modificado con éxito.")
    else:
        print("No se encontró el documento o no hubo cambios.")
    print('\nRegistros después de la actualización')
    for producto in productos:
        print(producto["nombre"], producto["categoria"], producto["precio"], producto["stock"])
        
    # Eliminar registros
    print('\nRegistros antes de la eliminación')
    for producto in productos:
        print(producto["nombre"], producto["categoria"], producto["precio"], producto["stock"])
    for producto in productos:
        resultado = coleccion.delete_many({"stock": 3})
    # Verificar si el documento fue eliminado
    if resultado.deleted_count > 0:
        print("Documento eliminado con éxito.")
    else:
        print("No se encontró el documento para eliminar.")  
    print('\nRegistros después de la eliminación')
    for producto in productos:
        print(producto["nombre"], producto["categoria"], producto["precio"], producto["stock"])
    
    
    
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
        
        