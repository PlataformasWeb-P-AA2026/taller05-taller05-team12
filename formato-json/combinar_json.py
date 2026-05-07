import json

archivos = ['sudamerica.json', 'europa.json', 'norteamerica_asia.json']
todos_los_docs = []

for archivo in archivos:
    with open(archivo, 'r', encoding='utf-8') as f:
        docs = json.load(f)
        todos_los_docs.extend(docs)

salida = {
    "docs": todos_los_docs
}

with open('mundial_2026.json', 'w', encoding='utf-8') as f:
    json.dump(salida, f, indent=4, ensure_ascii=False)
    
print(f"Generado mundial_2026.json final con {len(todos_los_docs)} registros en total.")
