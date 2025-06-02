import PyPDF2
import os

def unir_pdfs_en_carpeta(carpeta, ruta_salida):
    """
    Une todos los archivos PDF en una carpeta en un solo PDF.
    """
    pdf_writer = PyPDF2.PdfWriter()

    archivos_pdf = sorted([
        f for f in os.listdir(carpeta)
        if f.lower().endswith('.pdf') and os.path.isfile(os.path.join(carpeta, f))
    ])

    if not archivos_pdf:
        print("❌ No se encontraron archivos PDF en la carpeta.")
        return

    for nombre_archivo in archivos_pdf:
        ruta_completa = os.path.join(carpeta, nombre_archivo)
        try:
            with open(ruta_completa, 'rb') as archivo_pdf:
                pdf_reader = PyPDF2.PdfReader(archivo_pdf)
                if pdf_reader.is_encrypted:
                    try:
                        pdf_reader.decrypt('')
                    except:
                        print(f"⚠️ PDF cifrado no soportado: {nombre_archivo}")
                        continue

                for pagina in pdf_reader.pages:
                    pdf_writer.add_page(pagina)

        except Exception as e:
            print(f"⚠️ No se pudo procesar '{nombre_archivo}': {e}")
            continue

    try:
        with open(ruta_salida, 'wb') as salida_pdf:
            pdf_writer.write(salida_pdf)
        print(f"✅ PDFs unidos en '{ruta_salida}'")
    except Exception as e:
        print(f"❌ Error al guardar el archivo de salida: {e}")

# --- Ejecución interactiva ---
carpeta_con_pdfs = input("Introduce la ruta de la carpeta con los PDFs: ").strip()
salida_pdf = input("Introduce la ruta del archivo PDF de salida: ").strip()

unir_pdfs_en_carpeta(carpeta_con_pdfs, salida_pdf)
