import os
import time

def revisar_directorio(directorio):
    try:
        elementos = os.listdir(directorio)
    except PermissionError:
        print(f"⚠️ Sin permisos para leer: {directorio}")
        return

    for elemento in elementos:
        ruta_completa = os.path.join(directorio, elemento)
        if os.path.isdir(ruta_completa):
            revisar_directorio(ruta_completa)
        else:
            try:
                fecha_modificacion = os.path.getmtime(ruta_completa)
                if fecha_modificacion < (time.time() - 30 * 24 * 60 * 60):  # Archivos más antiguos que 30 días
                    print(f"🗑️ Borrando archivo antiguo: {ruta_completa}")
                    os.remove(ruta_completa)
            except Exception as e:
                print(f"⚠️ Error al procesar {ruta_completa}: {e}")
directorio = input("Introduce el directorio a revisar: ")
revisar_directorio(directorio)
