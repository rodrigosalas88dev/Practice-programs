
titulo = "BIENVENIDO AL TEST SOBRE EL QUESO"

print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: Que haces cuando ves una tabla de quesos?\n"
               "A - Salgo corriendo\n"
               "B - Pruebo uno de los quesos o incluso varios\n"
               "C - No puedo evitar devorarla\n")

if opcion == "A":
    puntuacion = puntuacion + 0
elif opcion == "B":
    puntuacion = puntuacion + 5
elif opcion == "C":
    puntuacion = puntuacion + 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

opcion = input("Pregunta 2: Como te gusta la hamburguesa?\n"
               "A - Sin queso\n"
               "B - Con queso\n"
               "C - Pan y queso\n")

if opcion == "A":
    puntuacion = puntuacion + 0
elif opcion == "B":
    puntuacion = puntuacion + 5
elif opcion == "C":
    puntuacion = puntuacion + 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

opcion = input("Pregunta 3: Sos intolerante a la lactosa?\n"
               "A - Si\n"
               "B - A veces\n"
               "C - No\n")

if opcion == "A":
    puntuacion = puntuacion + 0
elif opcion == "B":
    puntuacion = puntuacion + 5
elif opcion == "C":
    puntuacion = puntuacion + 10

else:
    print("Las opciones posibles son A, B y C")
    exit()

if puntuacion >= 25:
    print("Felicidades, te gusta el queso")
elif puntuacion >= 15:
    print("Felicidades, sos una persona que le gusta el queso")
else:
    print("Felicidades, no te gusta el queso")
