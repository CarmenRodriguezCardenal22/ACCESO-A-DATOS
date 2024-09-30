import json

class JSONFileHandler:
    def write_json(self, file_path):
        try:
            d = {"Dni": 30284233, "Fecha de nacimiento": "22/6/2004"}
            with open(file_path, 'w') as f:
                json.dump(d,f)
        except Exception as e:
            print(f"Error escribiendo JSON: {e}")
    
    def read_json(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error leyendo JSON: {e}")
# Uso
json_handler = JSONFileHandler()
data = json_handler.write_json('data.json')
data = json_handler.read_json('data.json')
print(data)