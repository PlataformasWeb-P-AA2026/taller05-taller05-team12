Evidencias Taller 05
Creacion de la base de datos dentro de couch DB llamada jugadores
![alt text](image.png)

Creacion de los tres scripts para transformarlos a Json
csv a json

```java
script
import pandas as pd
import json

df = pd.read_csv('../data/fuente_csv_sudamerica.csv')
docs = df.to_dict(orient='records')

with open('sudamerica.json', 'w', encoding='utf-8') as f:
    json.dump(docs, f, indent=4, ensure_ascii=False)
    
print(f"Generado sudamerica.json con {len(docs)} registros.")
```

```java
script
```

```java
script
```
