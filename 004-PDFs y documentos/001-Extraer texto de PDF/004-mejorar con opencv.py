import cv2
import pytesseract
from PIL import Image
import numpy as np

# Ruta al ejecutable de Tesseract (solo en Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Cargar la imagen con OpenCV
imagen_cv = cv2.imread("imagen.jpg")

# Convertir a escala de grises
gris = cv2.cvtColor(imagen_cv, cv2.COLOR_BGR2GRAY)

# Opcional: eliminar ruido con filtro mediano
suavizado = cv2.medianBlur(gris, 3)

# Aplicar umbral adaptativo para mejorar contraste
binaria = cv2.adaptiveThreshold(
    suavizado, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11, 2
)

# (Opcional) Guardar imagen preprocesada para revisar
cv2.imwrite("procesada.jpg", binaria)

# Convertir imagen binaria a formato PIL para pytesseract
imagen_pil = Image.fromarray(binaria)

# Aplicar OCR
texto = pytesseract.image_to_string(imagen_pil, lang="eng")

print("Texto detectado:")
print(texto)
