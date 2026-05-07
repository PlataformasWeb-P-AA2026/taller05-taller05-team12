Evidencias Taller 05
Creacion de la base de datos dentro de couch DB llamada jugadores
![alt text](image.png)

Creacion de los tres scripts para transformarlos a Json

```java
script csv a jason

import pandas as pd
import json

df = pd.read_csv('../data/fuente_csv_sudamerica.csv')
docs = df.to_dict(orient='records')

with open('sudamerica.json', 'w', encoding='utf-8') as f:
    json.dump(docs, f, indent=4, ensure_ascii=False)
    
print(f"Generado sudamerica.json con {len(docs)} registros.")
```

```java
script html a json

import pandas as pd

tablas = pd.read_html('../data/fuente_html_europa.html')

# Tomar la primera tabla
df = tablas[0]

# Renombrar columnas a minúsculas y ajustar "club" a "club_actual" para CouchDB
df.columns = [col.lower() for col in df.columns]
df = df.rename(columns={'club': 'club_actual'})

# Convertir a JSON
df.to_json('europa.json', orient='records', indent=4, force_ascii=False)
print("Tabla HTML convertida a JSON usando pandas.")
```

```java
script pdf a jason

import pdfplumber
import json

docs = []
headers = []

with pdfplumber.open("../data/fuente_pdf_norteamerica_asia.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            lines = text.strip().split('\n')
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                if not headers and parts[0].lower() == 'nombre':
                    headers = [p.lower() for p in parts]
                    continue

                if len(parts) >= 5:
                    row_dict = {
                        'nombre': parts[0],
                        'seleccion': parts[1],
                        'posicion': parts[2],
                        'edad': int(parts[3]),
                        'goles': int(parts[4])
                    }
                    docs.append(row_dict)

# Guardar en archivo JSON con la estructura correcta
with open("norteamerica_asia.json", "w", encoding='utf-8') as f:
    json.dump(docs, f, ensure_ascii=False, indent=4)

print(f"PDF convertido a JSON estructurado. Se extrajeron {len(docs)} registros.")
```

```java
script combinado de todos los Json

import pandas as pd
import json

df = pd.read_csv('../data/fuente_csv_sudamerica.csv')
docs = df.to_dict(orient='records')

with open('sudamerica.json', 'w', encoding='utf-8') as f:
    json.dump(docs, f, indent=4, ensure_ascii=False)
    
print(f"Generado sudamerica.json con {len(docs)} registros.")
```
para combinar todos los json hicimos uso de la herramienta bulldogs

Evidencias de cargas en couchDB
