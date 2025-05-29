print("Indica el tipo de conversión:")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")
opcion = input("Introduce la opción: ")
grados = input("Introduce los grados: ")
if opcion == "1":
    resultado = (float(grados) * 9/5) + 32
    print()
elif opcion == "2":
    resultado = (float(grados) - 32) * 5/9
print("Resultado: " + str(resultado))

