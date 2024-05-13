###### ESTE CODIGO HAY QUE REVISARLO #######



print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multiplicacion y division")

n1 = ""
while True:
    if not n1:
        n1 = input("Ingrese numero: ")
        if n1.lower() == "salir":
            break
        n1 = int(n1)
    op = input("Ingresa operacion: suma, resta, division o multiplicacion?: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        n1 += n2
    elif op.lower() == "resta":
        n1 -= n2
    elif op.lower() == "division":
        n1 /= n2
    elif op.lower() == "multiplicacion":
        n1 *= n2
    else:
        print("Comando no valido")
        break

print(f"El resultado es {n1}")
