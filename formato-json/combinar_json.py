import json

# Leer los archivos simultáneamente
with open('sudamerica.json', encoding='utf-8') as f1, \
     open('europa.json', encoding='utf-8') as f2, \
     open('norteamerica_asia.json', encoding='utf-8') as f3:
    data1 = json.load(f1)
    data2 = json.load(f2)
    data3 = json.load(f3)

resultado = data1 + data2 + data3

salida = {
    "docs": resultado
}

# Escribir el archivo final
with open('mundial_2026.json', 'w', encoding='utf-8') as f_out:
    json.dump(salida, f_out, ensure_ascii=False, indent=4)

print(f"Generado mundial_2026.json final con {len(resultado)} registros en total.")
