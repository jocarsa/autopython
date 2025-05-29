import pandas as pd

agenda = [
    ["Nombre", "Edad", "Ciudad"],
    ["Juan", 28, "Madrid"],
    ["Ana", 22, "Barcelona"],
    ["Luis", 35, "Valencia"],
    ["María", 30, "Sevilla"]
]
# Convertir la agenda a un DataFrame de pandas
df = pd.DataFrame(agenda[1:], columns=agenda[0])
# Guardar el DataFrame en un archivo Excel
archivo = "agenda.xlsx"

df.to_excel(archivo, index=False)
