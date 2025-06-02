import requests
from bs4 import BeautifulSoup as bs
# pip install bs4

contenido = requests.get("https://escuelamastermedia.es/cursos/").text
titulo = bs(contenido, "html.parser").find("title").text
print(titulo)
productos = bs(contenido, "html.parser").find_all("p", class_="elementor-heading-title elementor-size-default")
for producto in productos:
    print(producto.text.strip())