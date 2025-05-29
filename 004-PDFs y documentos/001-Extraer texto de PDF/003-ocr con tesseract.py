from PIL import Image
import pytesseract
# pip install pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

imagen = Image.open("imagen.jpg")

texto = pytesseract.image_to_string(imagen, lang="eng") 

print("Texto detectado:")
print(texto)