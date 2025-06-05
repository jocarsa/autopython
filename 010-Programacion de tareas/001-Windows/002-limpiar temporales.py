import os
import shutil

ruta_temp = "C:/Users/Admin/AppData/Local/Temp"
for archivo in os.listdir(ruta_temp):
    try:
        ruta = os.path.join(ruta_temp, archivo)
        if os.path.isfile(ruta):
            os.remove(ruta)
        elif os.path.isdir(ruta):
            shutil.rmtree(ruta)
    except Exception as e:
        print(f"Error eliminando {archivo}: {e}")
