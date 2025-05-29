class Contacto:
    def __init__(self):
        self.nombre = ""
        self.telefono = ""
        self.email = ""
        self.direccion = ""

agenda = []
while True:
    contacto = Contacto()
    contacto.nombre = input("Introduce el nombre del contacto: ")
    contacto.telefono = input("Introduce el telefono del contacto: ")
    contacto.email = input("Introduce el email del contacto: ")
    contacto.direccion = input("Introduce la direccion del contacto: ")
    
    agenda.append(contacto)
    
    print("\nAgenda de contactos:")
    for contacto in agenda:
        print(f"Nombre: {contacto.nombre}, Telefono: {contacto.telefono}, Email: {contacto.email}, Direccion: {contacto.direccion}")
    
   