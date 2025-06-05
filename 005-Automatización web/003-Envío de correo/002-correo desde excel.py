import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.utils import formataddr

# Configuración del remitente
sender = "info@jocarsa.com"
password = "$"
smtp_server = "smtp.ionos.es"
smtp_port = 465

# Cargar el archivo ODS
df = pd.read_excel("envioemail.ods", engine="odf")

# Recorrer cada fila del archivo
for index, row in df.iterrows():
    email = row["email"]
    nombre = row["nombre"]

    # Personalizar el mensaje
    cuerpo = f"""
Hola {nombre},

Este es un mensaje de prueba enviado automáticamente desde Python.
¡Gracias por formar parte de nuestra comunidad!

Saludos cordiales,
Jose Vicente Carratalá
"""

    # Crear el mensaje MIME
    msg = MIMEText(cuerpo, "plain", "utf-8")
    msg["Subject"] = "Hola desde Python"
    msg["From"] = formataddr(("Jocarsa", sender))
    msg["To"] = email

    # Enviar el mensaje
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender, password)
            server.sendmail(sender, email, msg.as_string())
        print(f"Correo enviado a {nombre} ({email})")
    except Exception as e:
        print(f"Error al enviar a {email}: {e}")
