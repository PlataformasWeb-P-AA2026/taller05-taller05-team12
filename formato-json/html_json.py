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
