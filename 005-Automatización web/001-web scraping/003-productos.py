import requests
from bs4 import BeautifulSoup as bs
# pip install bs4

contenido = requests.get("https://www.jocarsa.com/").text
titulo = bs(contenido, "html.parser").find("title").text
print(titulo)
productos = bs(contenido, "html.parser").find_all("h2")
for producto in productos:
    print(producto.text.strip())