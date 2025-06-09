import json
import PyPDF2

# Cargar el mapeado desde el archivo JSON externo
with open("mapeado.json", "r", encoding="utf-8") as f:
    mapeado = json.load(f)

# Leer el formulario PDF
with open("formulario.pdf", "rb") as archivo:
    lector = PyPDF2.PdfReader(archivo)
    campos = lector.get_fields()

# Mostrar campos con nombres descriptivos
for nombre, datos in campos.items():
    nombre_legible = mapeado.get(nombre, nombre)
    valor = datos.get("/V", "")
    print(f"{nombre_legible}: {valor}")
