import requests
import json

url_base = 'http://admin:admin@localhost:5984'
base_datos = "jugadores"
url = f"{url_base}/{base_datos}"
headers = {'Content-Type': 'application/json'}

with open('mundial_2026.json', 'r', encoding='utf-8') as f:
   
    data = json.load(f)

lista_datos = []

for d in data['docs']:
    lista_datos.append(d)

for doc in lista_datos:
    response = requests.post(
        url,
        json=doc,
        headers=headers
    )
    print(f"Insertando {doc.get('nombre', 'Desconocido')} | {response.status_code}")

design_doc = {
    "_id": "_design/losjugadores",
    "views": {
        "por_club": {
            "map": "function(doc) { if (doc.club_actual) { emit(doc.club_actual, doc); } }"
        },
        "por_goles": {
            "map": "function(doc) { if (doc.goles) { emit(doc.goles, doc); } }"
        },
        "por_partidos": {
            "map": "function(doc) { if (doc.partidos) { emit(doc.partidos, doc); } }"
        }
    }
}

response_vistas = requests.put(
    f"{url}/_design/losjugadores",
    json=design_doc,
    headers=headers
)

if response_vistas.status_code in [201, 202]:
    print("Vistas creadas exitosamente.")
elif response_vistas.status_code == 409:
    res_get = requests.get(f"{url}/_design/losjugadores")
    if res_get.status_code == 200:
        design_doc['_rev'] = res_get.json().get('_rev')
        requests.put(f"{url}/_design/losjugadores", json=design_doc, headers=headers)
        print("Vistas actualizadas exitosamente.")
