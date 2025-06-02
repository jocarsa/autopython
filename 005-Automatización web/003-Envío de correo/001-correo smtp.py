import smtplib
from email.mime.text import MIMEText

sender = "info@jocarsa.com"
receiver = "randymorales07@outlook.com"
password = "Jocarsa123$"

# Crear un mensaje MIME adecuado
msg = MIMEText("Este es un mensaje de prueba.")
msg["Subject"] = "Hola desde Python"
msg["From"] = sender
msg["To"] = receiver

# Enviar usando SSL
with smtplib.SMTP_SSL("smtp.ionos.es", 465) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
