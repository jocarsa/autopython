import cv2
import os
from PIL import Image

# Configuración
input_folder = "seleccion"
output_folder = "recortadas"
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Crear carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

def crop_centered_on_face(img_path, output_path):
    img_cv = cv2.imread(img_path)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) == 0:
        print(f"No face detected in {img_path}")
        return

    # Elegir la cara más grande
    x, y, w, h = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)[0]
    cx, cy = x + w // 2, y + h // 2

    # Calcular tamaño del recorte cuadrado (el doble del max entre w y h de la cara)
    face_size = max(w, h)
    crop_size = int(face_size * 2)

    img_h, img_w = img_cv.shape[:2]
    
    # Calcular límites del recorte sin salirse de la imagen
    left = max(0, cx - crop_size // 2)
    right = min(img_w, cx + crop_size // 2)
    top = max(0, cy - crop_size // 2)
    bottom = min(img_h, cy + crop_size // 2)

    # Ajustar para mantener 1:1 sin crear borde vacío
    crop_w = right - left
    crop_h = bottom - top
    final_size = min(crop_w, crop_h)

    # Reajustar centro si es necesario
    cx = (left + right) // 2
    cy = (top + bottom) // 2
    left = max(0, cx - final_size // 2)
    top = max(0, cy - final_size // 2)
    right = left + final_size
    bottom = top + final_size

    # Recortar y guardar
    cropped = img_cv[top:bottom, left:right]
    img_pil = Image.fromarray(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))
    img_pil.save(output_path)
    print(f"Saved: {output_path}")

# Procesar todas las imágenes
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        crop_centered_on_face(input_path, output_path)
