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
script
```
