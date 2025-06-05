import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.widgets import Entry, Button, Label
from ttkbootstrap.scrolled import ScrolledText
from openai import OpenAI

# Inicializa cliente OpenAI
client = OpenAI(api_key="")

# Función para enviar pregunta
def enviar_pregunta(event=None):
    texto = entrada.get()
    entrada.delete(0, tk.END)
    respuesta.delete("1.0", tk.END)
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": texto}]
        )
        respuesta_texto = response.choices[0].message.content
        respuesta.insert(tk.END, f"ChatGPT: {respuesta_texto}")
    except Exception as e:
        respuesta.insert(tk.END, f"Error: {e}")

# Estilo y ventana principal
style = Style(theme="superhero")  # Puedes probar: "flatly", "solar", "cosmo", etc.
ventana = style.master
ventana.title("ChatGPT Cliente")
ventana.geometry("600x400")
ventana.resizable(False, False)

# Widgets con ttkbootstrap
Label(ventana, text="Escribe tu pregunta:", font=("Helvetica", 14)).pack(anchor="w", padx=20, pady=(20, 5))
entrada = Entry(ventana, font=("Helvetica", 12), width=50)
entrada.pack(padx=20, fill="x")
entrada.bind("<Return>", enviar_pregunta)

Button(ventana, text="Enviar", bootstyle="success", command=enviar_pregunta).pack(pady=10)

respuesta = ScrolledText(ventana, height=10, font=("Consolas", 11))
respuesta.pack(padx=20, pady=(0, 20), fill="both", expand=True)

ventana.mainloop()
