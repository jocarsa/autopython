import json
import csv
import os
import PyPDF2

# Carpeta con los formularios PDF
carpeta = "formularios"

# Cargar el mapeado desde el archivo JSON externo
with open("mapa.json", "r", encoding="utf-8") as f:
    mapeado = json.load(f)

# Lista para almacenar todas las filas (diccionarios)
resultados = []

# Recorrer todos los archivos PDF de la carpeta
for archivo_pdf in os.listdir(carpeta):
    if archivo_pdf.endswith(".pdf"):
        ruta_pdf = os.path.join(carpeta, archivo_pdf)
        with open(ruta_pdf, "rb") as archivo:
            lector = PyPDF2.PdfReader(archivo)
            campos = lector.get_fields()

            fila = {}
            for nombre, datos in campos.items():
                nombre_legible = mapeado.get(nombre, nombre)
                valor = datos.get("/V", "")
                fila[nombre_legible] = valor
            fila["archivo"] = archivo_pdf  # Nombre del archivo como referencia
            resultados.append(fila)

# Obtener todas las claves únicas para las columnas del CSV
todas_las_claves = set()
for fila in resultados:
    todas_las_claves.update(fila.keys())
todas_las_claves = sorted(todas_las_claves)

# Escribir el archivo CSV
with open("resultados.csv", "w", newline="", encoding="utf-8") as fcsv:
    escritor = csv.DictWriter(fcsv, fieldnames=todas_las_claves)
    escritor.writeheader()
    for fila in resultados:
        escritor.writerow(fila)

print("✅ Datos extraídos y guardados en 'resultados.csv'")
