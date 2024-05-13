
opcion = input("Elige el tipo de movil: IOS[I] o Android[A]")

movil_ideal = "Ninguno"

if opcion == "A":  #Ha contestado Android
    opcion = input("Tienes dinero [S/N]?")

    if opcion == "S":  #Si tiene dinero
        opcion = input("Te importa la camara? [S/N]")

        if opcion == "S":  #Le importa la camara
            movil_ideal = "Google Pixel Supercamara"

        else:  #No le importa la camara
            movil_ideal = "Android calidad-precio"

    else:  #No tiene dinero
        movil_ideal = "Android Chino de €100"

elif opcion == "I":  #Ha contestado IOS
    opcion = input("Tienes dinero? [S/N]?")

    if opcion == "S":  #Tiene dinero
        movil_ideal = "iPhone Pro Ultra Max"

    else:  #No tiene dinero
        movil_ideal = "iPhone de segunda mano"

print("Tu movil ideal es: " + movil_ideal)





