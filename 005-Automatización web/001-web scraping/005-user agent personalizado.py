import requests
from bs4 import BeautifulSoup as bs
# pip install bs4

cabeceras = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"
}

url = "https://escuelamastermedia.es/cursos/"
respuesta = requests.get(url, headers=cabeceras)
contenido = respuesta.text
titulo = bs(contenido, "html.parser").find("title").text
print(titulo)
productos = bs(contenido, "html.parser").find_all("p", class_="elementor-heading-title elementor-size-default")
for producto in productos:
    print(producto.text.strip())