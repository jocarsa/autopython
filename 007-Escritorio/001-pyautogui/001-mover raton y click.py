import pyautogui
import time

#mover_raton = pyautogui.moveTo(100, 100, duration=1)  # Mueve el ratón a la posición (100, 100) en 1 segundo
#click_raton = pyautogui.click()  # Realiza un clic en la posición actual del ratón
while True:
    tupla = pyautogui.position()
    print(tupla)  # Imprime la posición actual del ratón
    time.sleep(1)  # Espera 1 segundo antes de volver a imprimir la posición