listadelacompra = []
while True:
    producto = input("Introduce el nombre del producto: ")
    precio = input("Introduce el precio del producto: ")
    listadelacompra.append((producto,float(precio)))
    suma = 0.0
    for elemento in listadelacompra:
        print(elemento[0]+" "*(20-len(elemento[0]))+str(elemento[1])+"€")
        suma = suma + elemento[1]
    print(f"Total: {suma} €")