import pywhatkit as kit
import pyautogui
import time

numero = "+34619049777"
mensaje = "¡Hola! Esto es un mensaje automático de prueba :)"

# Envía mensaje a las 16:30 (debes programar al menos 2 minutos en el futuro)
kit.sendwhatmsg(numero, mensaje, 10, 47)

# Espera unos segundos a que el mensaje esté preparado (ajusta si es necesario)
time.sleep(15)

# Pulsa "Enter" para enviarlo automáticamente
pyautogui.press("enter")
