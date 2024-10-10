import random

numero_secreto = random.randint(1, 100)
contador_intentos = 0

while True:
    contador_intentos += 1
    numero_ingresado = int(input("Ingrese un numero entero: "))
    if numero_ingresado == numero_secreto:
        print(f"Usted GANO en {contador_intentos} intentos!")
        break
    elif numero_ingresado < numero_secreto:
        print("El numero secreto es MAYOR")
    else:
        print("El numero secreto es MENOR")