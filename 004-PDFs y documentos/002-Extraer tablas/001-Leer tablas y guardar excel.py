import pdfplumber
import pandas as pd

# pip install pdfplumber pandas openpyxl

archivo_pdf = "documento.pdf"
tablas_extraidas = []

with pdfplumber.open(archivo_pdf) as pdf:
    for pagina in pdf.pages:
        tablas = pagina.extract_tables()
        for tabla in tablas:
            tablas_extraidas.append(tabla)

# Guardar cada tabla en una hoja de Excel diferente
archivo_excel = "tablas_extraidas.xlsx"
with pd.ExcelWriter(archivo_excel, engine='openpyxl') as writer:
    for i, tabla in enumerate(tablas_extraidas):
        df = pd.DataFrame(tabla)
        df.to_excel(writer, sheet_name=f"Tabla_{i+1}", index=False)

print(f"\n✅ {len(tablas_extraidas)} tablas guardadas en '{archivo_excel}'")
