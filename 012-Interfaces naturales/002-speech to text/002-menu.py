import speech_recognition as sr
from gtts import gTTS
import os
import tempfile

clientes = {}

def hablar(texto):
    tts = gTTS(text=texto, lang='es')
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
        tts.save(fp.name)
        mp3_file = fp.name
    os.system(f'mpg123 "{mp3_file}" > /dev/null 2>&1')
    os.remove(mp3_file)

def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        hablar("Habla ahora")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language="es-ES")
        return texto.lower()
    except:
        hablar("No entendí. Intenta de nuevo.")
        return ""

def crear_cliente():
    hablar("Di el nombre del cliente")
    nombre = escuchar()
    hablar("Di el ID del cliente")
    id_cliente = escuchar()
    clientes[id_cliente] = nombre
    hablar(f"Cliente {nombre} con ID {id_cliente} creado.")

def listar_clientes():
    if clientes:
        for id, nombre in clientes.items():
            hablar(f"ID: {id}, Nombre: {nombre}")
    else:
        hablar("No hay clientes.")

def actualizar_cliente():
    hablar("Di el ID del cliente a actualizar")
    id_cliente = escuchar()
    if id_cliente in clientes:
        hablar("Di el nuevo nombre del cliente")
        nuevo_nombre = escuchar()
        clientes[id_cliente] = nuevo_nombre
        hablar("Cliente actualizado.")
    else:
        hablar("Cliente no encontrado.")

def eliminar_cliente():
    hablar("Di el ID del cliente a eliminar")
    id_cliente = escuchar()
    if id_cliente in clientes:
        del clientes[id_cliente]
        hablar("Cliente eliminado.")
    else:
        hablar("Cliente no encontrado.")

def menu():
    while True:
        hablar("¿Qué quieres hacer? Di crear, listar, actualizar, eliminar o salir.")
        opcion = escuchar()

        if "crear" in opcion:
            crear_cliente()
        elif "listar" in opcion:
            listar_clientes()
        elif "actualizar" in opcion:
            actualizar_cliente()
        elif "eliminar" in opcion:
            eliminar_cliente()
        elif "salir" in opcion:
            hablar("Hasta luego.")
            break
        else:
            hablar("Opción no válida.")

menu()
