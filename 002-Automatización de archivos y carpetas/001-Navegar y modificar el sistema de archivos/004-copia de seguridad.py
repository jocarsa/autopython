import os
import time
import shutil

def copia_seguridad(carpeta_origen,carpeta_destino):
    for carpeta_actual, subcarpetas, archivos in os.walk(carpeta_origen):
        ruta_relativa = os.path.relpath(carpeta_actual, carpeta_origen)
        destino_actual = os.path.join(carpeta_destino, ruta_relativa)

        if not os.path.exists(destino_actual):
            os.makedirs(destino_actual)

        for archivo in archivos:
            origen_archivo = os.path.join(carpeta_actual, archivo)
            destino_archivo = os.path.join(destino_actual, archivo)
            shutil.copy2(origen_archivo, destino_archivo)  # copy2 mantiene metadatos
            print(f"📁 Copiado: {origen_archivo} ➡️ {destino_archivo}")

# Ejemplo de uso
origen = input("Introduce la carpeta de origen: ")
destino =  "C:\\copias_seguridad\\" + time.strftime("%Y%m%d-%H%M%S")+"\\"
copia_seguridad(origen, destino)
