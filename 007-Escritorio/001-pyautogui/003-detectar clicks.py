from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Click detectado en: ({x}, {y})")

# Inicia el listener de eventos del ratón
with mouse.Listener(on_click=on_click) as listener:
    print("Escuchando clics... Pulsa Ctrl+C para salir.")
    listener.join()
