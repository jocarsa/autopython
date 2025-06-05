import imaplib
import email
from email.header import decode_header

# Configuración de la cuenta
imap_host = 'imap.ionos.es'       # Cambia esto si usas otro proveedor
correo = 'mastermedia@jocarsa.com'
contraseña = '$'

# Conectarse al servidor y hacer login
mail = imaplib.IMAP4_SSL(imap_host)
mail.login(correo, contraseña)

# Seleccionar el buzón de entrada
mail.select("inbox")

# Buscar los últimos 5 correos
status, mensajes = mail.search(None, "ALL")
id_mensajes = mensajes[0].split()
ultimos = id_mensajes[-5:]  # últimos 5 correos

for num in ultimos:
    # Buscar el correo por ID
    status, datos = mail.fetch(num, "(RFC822)")
    for respuesta in datos:
        if isinstance(respuesta, tuple):
            # Analizar el mensaje
            msg = email.message_from_bytes(respuesta[1])
            asunto, codificacion = decode_header(msg["Subject"])[0]
            if isinstance(asunto, bytes):
                asunto = asunto.decode(codificacion or "utf-8")
            remitente = msg.get("From")
            print(f"De: {remitente}")
            print(f"Asunto: {asunto}")

            # Si el mensaje tiene partes (texto, HTML, adjuntos)
            if msg.is_multipart():
                for parte in msg.walk():
                    tipo_contenido = parte.get_content_type()
                    disp = str(parte.get("Content-Disposition"))
                    if tipo_contenido == "text/plain" and "attachment" not in disp:
                        cuerpo = parte.get_payload(decode=True).decode()
                        print("Cuerpo:", cuerpo)
                        break
            else:
                # Si el mensaje es solo texto
                cuerpo = msg.get_payload(decode=True).decode()
                print("Cuerpo:", cuerpo)
            print("-" * 50)

# Cerrar la conexión
mail.logout()
