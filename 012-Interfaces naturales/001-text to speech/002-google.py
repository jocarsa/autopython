from gtts import gTTS
import os

# Texto que deseas leer
texto = "Hola, esto es una prueba de lectura automática con Python y la librería de Google."

# Crear el objeto de texto a voz
tts = gTTS(text=texto, lang='es')  # 'es' para español

# Guardar el resultado como archivo MP3
tts.save("salida.mp3")

# Reproducir el archivo (en Windows)
os.system("start salida.mp3")

# Para Linux usa:
# os.system("mpg123 salida.mp3")

# Para macOS usa:
# os.system("afplay salida.mp3")
