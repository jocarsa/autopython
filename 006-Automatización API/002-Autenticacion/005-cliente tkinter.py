import os
from openai import OpenAI
import tkinter as tk

client = OpenAI(api_key="")

def enviar_pregunta():
    pregunta_texto = pregunta.get()
    pregunta.delete(0, tk.END)
    respuesta.delete(1.0, tk.END)  # Limpiar la respuesta anterior
    response = client.responses.create(
        model="gpt-4o",
        input=pregunta_texto
    )
    respuesta_texto = response.output_text
    respuesta.insert(tk.END, "ChatGPT: " + respuesta_texto)  # Mostrar la respuesta en el Text widget
    
ventana = tk.Tk()
ventana.title("ChatGPT Cliente")

pregunta = tk.Entry(ventana, width=50)
pregunta.pack(pady=10)  
respuesta = tk.Text(ventana, height=10, width=50)
respuesta.pack(pady=10)

pregunta.bind("<Return>", lambda event: enviar_pregunta())
ventana.mainloop()

    