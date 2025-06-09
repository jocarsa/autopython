import pyttsx3

texto = "Aquí puedes poner el texto que quieras."
voz = pyttsx3.init()
voz.say(texto)
voz.runAndWait()
