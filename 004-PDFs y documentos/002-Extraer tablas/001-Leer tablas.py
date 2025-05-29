import pdfplumber

# pip install pdfplumber

archivo_pdf = "documento.pdf"
tablas_extraidas = []

with pdfplumber.open(archivo_pdf) as pdf:
    for pagina in pdf.pages:
        tablas = pagina.extract_tables()
        for tabla in tablas:
            tablas_extraidas.append(tabla)

# Mostrar las tablas extraídas
for i, tabla in enumerate(tablas_extraidas):
    print(f"\nTabla {i + 1}:")
    for fila in tabla:
        print(fila)