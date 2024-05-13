import random

numero_correcto = random.randint(1, 10)

numero_elegido = int(input("Adivina un numero del 1 al 10:"))
print (numero_elegido)

if numero_correcto == numero_elegido:
    print("Adivinaste!")

if numero_elegido < 1:
    print("Te quedaste corto")

if numero_elegido > 10:
    print("Te re pasaste")

if numero_elegido == 22:
    print("Parece ser que estas loco")

print("El numero ganador era: {}".format(numero_correcto))