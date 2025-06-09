from PIL import Image
import os

imagenes = [img for img in os.listdir() if img.endswith((".jpg", ".png"))]
imagenes.sort()
imagenes_pil = [Image.open(img).convert("RGB") for img in imagenes]

if imagenes_pil:
    imagenes_pil[0].save("salida.pdf", save_all=True, append_images=imagenes_pil[1:])
    print("✅ PDF generado como salida.pdf")
else:
    print("❌ No hay imágenes válidas.")
