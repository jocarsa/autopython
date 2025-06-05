import imaplib
import email
from email.header import decode_header
import os
import sys

# Configuración del correo
imap_host = 'imap.ionos.es'
correo = 'mastermedia@jocarsa.com'
contraseña = '$'

# Conexión IMAP
mail = imaplib.IMAP4_SSL(imap_host)
mail.login(correo, contraseña)
mail.select("inbox")

# Obtener el último correo
status, mensajes = mail.search(None, "ALL")
ids = mensajes[0].split()
if ids:
    ultimo_id = ids[-1]
    status, datos = mail.fetch(ultimo_id, "(RFC822)")

    for respuesta in datos:
        if isinstance(respuesta, tuple):
            msg = email.message_from_bytes(respuesta[1])
            asunto, codificacion = decode_header(msg["Subject"])[0]
            if isinstance(asunto, bytes):
                asunto = asunto.decode(codificacion or "utf-8")
            remitente = msg.get("From")

            # Obtener el cuerpo
            cuerpo = ""
            if msg.is_multipart():
                for parte in msg.walk():
                    tipo = parte.get_content_type()
                    disp = str(parte.get("Content-Disposition"))
                    if tipo == "text/plain" and "attachment" not in disp:
                        cuerpo = parte.get_payload(decode=True).decode(errors="ignore")
                        break
            else:
                cuerpo = msg.get_payload(decode=True).decode(errors="ignore")

            # Limpiar espacios en blanco
            cuerpo = cuerpo.strip()

            # Escribir en archivo
            with open("ultimo_correo.txt", "w", encoding="utf-8") as f:
                f.write(f"De: {remitente}\n")
                f.write(f"Asunto: {asunto}\n")
                f.write("Cuerpo:\n")
                f.write(cuerpo)

            # Verificar si debe apagarse
            if cuerpo.lower() == "shutdown":
                print("Comando 'shutdown' recibido. Apagando el sistema...")
                if sys.platform.startswith("win"):
                    os.system("shutdown /s /t 1")
                elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
                    os.system("shutdown now")
                else:
                    print("Sistema operativo no compatible.")

mail.logout()
