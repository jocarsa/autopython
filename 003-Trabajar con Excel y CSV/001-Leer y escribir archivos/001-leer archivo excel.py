import pandas as pd
import os

# pip install pandas openpyxl
directorioactual = os.getcwd()
archivo = os.path.join(directorioactual,'datos.xlsx')
contenido = pd.read_excel(archivo, engine='openpyxl')
print(contenido)