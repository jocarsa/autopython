import PyPDF2

# pip install pypdf2

archivo_pdf = 'documento.pdf'
archivo = open('documento.pdf', 'rb')
lector = PyPDF2.PdfReader(archivo) 
texto = ""
for pagina in lector.pages:
    texto += pagina.extract_text() + '\n'

print(texto)