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
