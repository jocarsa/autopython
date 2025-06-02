import requests
from bs4 import BeautifulSoup as bs
# pip install bs4

contenido = requests.get("https://www.jocarsa.com/").text
titulo = bs(contenido, "html.parser").find("title").text
print(titulo)