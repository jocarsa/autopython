import pandas as pd
import os

# pip install pandas openpyxl
directorioactual = os.getcwd()
archivo = os.path.join(directorioactual,'precios.xlsx')
contenido = pd.read_excel(archivo, engine='openpyxl')
for indice, fila in contenido.iterrows():
    nuevoprecio = fila['precio'] * 1.05
    contenido.at[indice, 'precio'] = nuevoprecio
contenido.to_excel(archivo, index=False, engine='openpyxl')
