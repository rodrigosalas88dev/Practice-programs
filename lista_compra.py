
lista_compra = []
input_usuario = None

print("PROGRAMA LISTA DE LA COMPRA\n"
      "---------------------------\n")

while input_usuario != "Q":
    input_usuario = input("¿Que desea comprar? (Q) para salir:")
    if input_usuario == "Q":
        pass
    elif input_usuario in lista_compra:
        print(f"{input_usuario} ya está en la lista")
    else:
        if input(f"¿Seguro que desea añadir {input_usuario} a la lista de la compra? (S/N)") == "S":
            lista_compra.append(input_usuario)

print("La lista de la compra es:")
print(lista_compra)

