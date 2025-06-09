import speech_recognition as sr

# Crear un reconocedor
r = sr.Recognizer()

# Usar el micrófono como fuente de audio
with sr.Microphone() as source:
    print("Di algo en español...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    try:
        # Usar Google para reconocer el audio (idioma español)
        texto = r.recognize_google(audio, language="es-ES")
        print("Has dicho:", texto)
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print(f"No se pudo conectar con Google Speech API: {e}")
