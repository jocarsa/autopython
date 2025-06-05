import time

hoy = time.localtime()
with open("C:/xampp/htdocs/autopython/010-Programacion de tareas/001-Windows/fecha.txt", "a") as archivo:
    archivo.write(f"{hoy.tm_year}-{hoy.tm_mon:02d}-{hoy.tm_mday:02d} {hoy.tm_hour:02d}:{hoy.tm_min:02d}:{hoy.tm_sec:02d}\n")
