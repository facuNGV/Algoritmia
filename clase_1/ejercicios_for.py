"""
1. Mostrar los números ascendentes desde el 1 al 10
for i in range(1,11):
    print(i)
"""
"""
2. Mostrar los números descendentes desde el 10 al 1
for i in range(10,0, -1):
    print(i)
"""
"""
3. Ingresar un número. Mostrar los números desde 0 hasta el número
ingresado.
numero = int(input("Ingrese un número: "))
while numero == 0:
    numero = int(input("Ingrese un número(distinto de 0): "))
    
if numero > 0:
    for i in range(numero):
        print(i)
elif numero < 0:
    for i in range(0, numero, -1):
        print(i)
"""
"""
4. Ingresar un número y mostrar la tabla de multiplicar de ese número. Por
ejemplo si se ingresa el numero 5:
5 x 0 = 0
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15 …
numero = int(input("Ingrese un número: "))

for i in range(11):
    print(f"{numero} x {i} = {numero*i}")
"""
"""
5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el
número 0. Mostrar la suma y el promedio de todos los números.
acumulador = 0
contador = 0
for i in range(10):
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    acumulador += numero
    contador += 1
print(f"La suma de todos los número es: {acumulador}, y el promedio es: {acumulador / contador}")
"""
"""
6. Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)
for i in range(1, 11):
    if i % 3 == 0:
        print(i)
"""
"""
7. Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
for i in range(1, 50):
    if i % 2 == 0:
        print(i)
"""
"""
8. Realizar un programa que permita mostrar una pirámide de números. Por
ejemplo: si se ingresa el numero 5, la salida del programa será la
siguiente:
1
12
123
1234
12345
numero = int(input("Ingrese un número: "))
acumulador_str = ""
for i in range(1, numero+1):
    acumulador_str += str(i)
    print(acumulador_str)
"""
"""
9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
el número ingresado. Mostrar la cantidad de divisores encontrados.
numero = int(input("Ingrese un número: "))
cantidad_divisores = 0
for i in range(1,numero):
    if numero % i == 0:
        print(i)
        cantidad_divisores += 1
print(f"Divisores encontrados: {cantidad_divisores}")
"""
"""
10.Ingresar un número. Determinar si el número es primo o no.
numero = int(input("Ingrese un número: "))
while numero != 0:
    contador_divisores = 0

    for i in range(1, numero+1):
        if numero % i == 0:
            contador_divisores += 1
    if contador_divisores == 2:
        print("El número es primo")
    else:
        print("El número no es primo")
    numero = int(input("Ingrese un número: "))
"""
"""
11. Ingresar un número. Mostrar cada número primo que hay entre el 1 y el
número ingresado. Informar cuántos números primos se encontraron.
num = int(input("Ingrese un número: "))

contador_primos = 0

for i in range(1, num):
	contador_resto_cero = 0
	for j in range(1, i+1):
		if i % j == 0:
			contador_resto_cero += 1
	if contador_resto_cero == 2:
		print(f"{i} es primo")
		contador_primos += 1

print(f"Se encontraron {contador_primos} primos")
"""