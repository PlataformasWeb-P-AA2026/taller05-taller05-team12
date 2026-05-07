import requests
import json

url_base = 'http://127.0.0.1:5985'
base_datos = "jugadores"
url = f"{url_base}/{base_datos}"
headers = {'Content-Type': 'application/json'}

with open('mundial_2026.json', 'r', encoding='utf-8') as f:
   
    data = json.load(f)

lista_datos = []

for d in data['docs']:
    lista_datos.append(d)
# bulk
url_bulk = f"{url}/_bulk_docs"
datos_finales = {'docs': lista_datos}
response_bulk = requests.post(url_bulk, headers=headers, json=datos_finales)

print(f"Inserción masiva finalizada. Código: {response_bulk.status_code}")

