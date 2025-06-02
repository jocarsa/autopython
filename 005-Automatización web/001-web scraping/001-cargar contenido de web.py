import requests

contenido = requests.get("https://www.jocarsa.com/").text
print(contenido)