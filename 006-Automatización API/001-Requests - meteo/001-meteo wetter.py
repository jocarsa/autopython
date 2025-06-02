import requests

ciudad = "Valencia"
url = f"https://wttr.in/{ciudad}?format=j1"

response = requests.get(url)

if response.status_code == 200:
    datos = response.json()
    hoy = datos["weather"][0]
    print(f"Predicción para hoy en {ciudad}:")
    print(f"Temperatura máxima: {hoy['maxtempC']} °C")
    print(f"Temperatura mínima: {hoy['mintempC']} °C")
    print(f"Descripción: {hoy['hourly'][0]['weatherDesc'][0]['value']}")
    print(datos)
else:
    print("Error al obtener los datos")

