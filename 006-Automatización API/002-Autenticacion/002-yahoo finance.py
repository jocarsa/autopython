import requests

API_KEY = 'TU_API_KEY_AQUI'
endpoint = 'https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/46250'  # Código INE de Valencia

# Paso 1: Solicitar el recurso
headers = {"Accept": "application/json"}
params = {"api_key": API_KEY}

response = requests.get(endpoint, headers=headers, params=params)

if response.status_code == 200:
    datos = response.json()

    # Paso 2: Obtener URL de los datos reales
    url_datos = datos.get("datos")

    # Paso 3: Descargar los datos reales
    response_datos = requests.get(url_datos)
    if response_datos.status_code == 200:
        datos_json = response_datos.json()
        print("Predicción para hoy:")
        print(datos_json[0]["prediccion"]["dia"][0])
    else:
        print("Error al obtener los datos reales.")
else:
    print("Error en la solicitud:", response.status_code)
