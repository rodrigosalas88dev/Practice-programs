
print("Bienvenido a la Conversion Divisa")

dolar_euro = 0.91
libra_euro = 1.18

opcion = input("Que opcion desea hacer?\n"
               "A - Convertir de dolar a euro\n"
               "B - Convertir de euro a dolar\n"
               "C - Convertir de libra a euro\n"
               "D - Convertir de euro a libra\n")

texto_usuario = "Introduzca la cantidad {} a convertir: "

if opcion == "A":
    cantidad_de_dinero = float(input(texto_usuario.format("dolares")))
    print("La cantidad en euros es: {}".format(cantidad_de_dinero * dolar_euro))

elif opcion == "B":
    cantidad_de_dinero = float(input(texto_usuario.format("euros")))
    print("La cantidad en dolares es: {}".format(cantidad_de_dinero / dolar_euro))

elif opcion == "C":
    cantidad_de_dinero = float(input(texto_usuario.format("libras")))
    print("La cantidad en euros es: {}".format(cantidad_de_dinero * dolar_euro))

elif opcion == "D":
    cantidad_de_dinero = float(input(texto_usuario.format("euros")))
    print("La cantidad en libras es: {}".format(cantidad_de_dinero / dolar_euro))

else:
    print("No ha elegido ninguna opcion valida")