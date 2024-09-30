import csv
import json

class FileConverter:
    def json_to_csv(self, csv_file, json_file):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)                  
                # Si 'data' es un diccionario (no una lista), lo convertimos en una lista con un único elemento
                if isinstance(data, dict):
                    data = [data]
                
                # Verificar que 'data' sea una lista de diccionarios
                # Si no es una lista o no contiene únicamente diccionarios, lanza un error
                if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
                    raise ValueError("El archivo JSON no contiene una lista de diccionarios.")
            
            # Obtener las claves del primer diccionario de la lista para usarlas como encabezados del CSV
            fieldnames = data[0].keys()

            with open(csv_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)  
                writer.writeheader()
                writer.writerows(data)  
                print(f'Conversión de {json_file} a {csv_file} completada.')  
        except Exception as e:
            
            print(f"Error en la conversión: {e}")

converter = FileConverter()
converter.json_to_csv('data.csv', 'data.json')


