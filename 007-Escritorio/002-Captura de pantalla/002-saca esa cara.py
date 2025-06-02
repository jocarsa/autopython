import cv2
import numpy as np
import pyautogui
import time

time.sleep(5)  # Espera 5 segundos para que puedas prepararte

# Tomar captura de pantalla
screenshot = pyautogui.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Cargar el clasificador de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Convertir a escala de grises
gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

# Detectar rostros
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Mostrar recortes de caras reconocidas
if len(faces) > 0:
    print(f"Detected {len(faces)} face(s).")
    for i, (x, y, w, h) in enumerate(faces):
        face_img = screenshot[y:y+h, x:x+w]
        cv2.imshow(f'Face {i+1}', face_img)
        cv2.rectangle(screenshot, (x, y), (x+w, y+h), (0, 255, 0), 2)
else:
    print("No faces detected.")

# Mostrar la imagen original con los rostros marcados
cv2.imshow('Screenshot with Face Detection', screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()
