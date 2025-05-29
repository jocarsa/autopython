import PyPDF2

# pip install pypdf2
busqueda = input("Introduce el término de búsqueda: ")
archivo = open('libro.pdf', 'rb')
lector = PyPDF2.PdfReader(archivo) 
texto = ""

for i, pagina in enumerate(lector.pages, start=1):
    texto_pagina = pagina.extract_text()
    if texto_pagina and busqueda.lower() in texto_pagina.lower():
        texto += f"\n\n--- Página {i} ---\n"

archivo.close()
print(texto)
