import random
from MisFunciones import *
# 1) Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.
def sumar_enteros(lista:list) -> int:
    """
    """
    acumulador = 0
    for numero in lista: # [4, 5, 6, 7, 8]
        acumulador += numero

    return acumulador

# lista = [4, 5, 6, 7, 8]

# 2) Definir una lista que almacene los nombres de los primeros seis meses del año. Mostrar el primer y último elemento de la lista solamente.
# meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
def mostrar_meses(lista:list, indice:int) -> None:
    """
    """
    print(lista[indice])

# mostrar_meses(meses, 2)
# mostrar_meses(meses, 3)


# 3) Definir una lista que almacene como primer elemento el nombre de un alumno y en las dos siguientes sus notas. Imprimir luego el nombre y el promedio de las dos notas.
# lista5 = ["Tomás", 10, 8]

def informar_nombre_promedio(lista:list) -> None:
    """
    """
    suma = lista[1] + lista[2]
    promedio = suma / 2
    print(f"Nombre del alumno: {lista[0]}\nPromedio: {promedio}")

# informar_nombre_promedio(lista5)


# 4)
def contar_cantidad_numeros_superiores(lista:list, valor_minimo:int)->int:
    contador = 0
    for numero in lista:
        if numero > valor_minimo:
            contador+=1
    return contador


# 5)
def mostrar_valores_iguales_o_superiores(lista:list, valor_minimo:int)->None:
    """
    """
    for numero in lista:
        if numero >= valor_minimo:
            print(numero)


# 6)
def generar_lista_aleatoria_numeros(cantidad_numeros:int, minimo:int, maximo:int)->list:
    """
    """
    lista_numeros = []
    for _ in range(cantidad_numeros):
        lista_numeros += [random.randint(minimo, maximo)]
    return lista_numeros


def mostrar_cantidad_pares(lista:list)->int:
    """
    """
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    return contador


# 7)
def medir_coleccion(coleccion:list|str)->int:
    """
    """
    contador = 0
    for _ in coleccion:
        contador += 1
    
    return contador

def determinar_nombres_mas_de_5_caracteres(lista_nombres:list)->int:
    """
    """
    contador_palabras = 0

    for i in range(medir_coleccion(lista_nombres)):
        if medir_coleccion(lista_nombres[i]) >= 5:
            contador_palabras += 1
    
    return contador_palabras
# 8)
def solicitar_numero(longitud_lista:int)->list:
    """
    """
    lista = []

    for i in range(longitud_lista):
        numero = int(input(f"Ingrese numero{i + 1}: "))
        lista += [numero]

    return lista


def imprimir_lista(lista:list)->None:
    """
    """
    for i in range(medir_coleccion(lista)):
        if i != (medir_coleccion(lista) - 1):
            print(lista[i])


# 9)
def pedir_elementos_para_lista(mensaje:str, dato_de_corte:int=0)->list:
    """
    """
    lista = []
    while numero != dato_de_corte:
        numero = int(input(mensaje))
        lista += [numero]
    return lista

def muestro_lista(lista:list)->None:
    """
    """
    for elemento in lista:
        print(elemento)
    print(f"el largo de la lista es: {medir_coleccion(lista)}")
# lista = pedir_elementos_para_lista("Ingrese numeros(0 para terminar): ")

# 10)
def almacenar_numeros_en_lista(mensaje:str, cantidad:int)->list:
    lista = [None] * cantidad
    for i in range(medir_coleccion(lista)):
        lista[i] = float(input(mensaje))
    return lista


def calcular_promedio_lista(lista:list)->float:
    """
    """
    acu = 0
    for elemento in lista:
        acu += elemento
    promedio = acu / medir_coleccion(lista)
    return promedio
# lista = almacenar_numeros_en_lista(7)
# muestro_lista(lista)
# print(f"el promedio de sueldo entre operarios es de: {calcular_promedio_lista(lista)}")


# 11)
def contar_alturas_superior_promedio(promedio:float, lista:list)->int:
    """
    """
    contador = 0
    for elemento in lista:
        if elemento > promedio:
            contador += 1
    return contador

# lista_ej11 = almacenar_numeros_en_lista(cantidad=5, mensaje="Ingrese altura: ")
# promedio = calcular_promedio_lista(lista_ej11)
# alturas_superiores_al_promedio = contar_alturas_superior_promedio(promedio, lista_ej11)
# print(f"Promedio de alturas: {promedio:.2f}\nHay {alturas_superiores_al_promedio} personas que superan el promedio")


# 12)
def cargar_lista_con_enteros(cantidad:int, mensaje:str)->list:
    """
    """
    lista = []
    for _ in range(cantidad):
        numero = int(input(mensaje))
        lista += [numero]
    return lista


def identificar_mayor_entero_de_lista(lista:list)->int|None:
    """
    """
    minimo = None
    for numero in lista:
        if minimo == None or numero > minimo:
            minimo = numero
    return minimo


# 13)
def identificar_menor_entero_de_lista(lista:list)->int|None:
    """
    """
    minimo = None
    for numero in lista:
        if minimo == None or numero < minimo:
            minimo = numero
    return minimo


def identificar_posicion(lista:list, elemento:int)->int|None:
    """
    Busca la primera ocurrencia de un valor
    Retorna: su posición o índice
    """
    for i in range(medir_coleccion(lista)):
        if lista[i] == elemento:
            return i
# lista_generada = cargar_lista_con_enteros(5, "Ingrese numero entero: ")
# minimo_de_la_lista = identificar_menor_entero_de_lista(lista_generada)
# posicion_identificada = identificar_posicion(lista_generada, minimo_de_la_lista)
# print(f"La posicion del minimo encontrado en la lista es: {posicion_identificada}")


# 14)
def cargar_lista_con_str(cantidad:int, mensaje:str)->list:
    """
    """
    #copiar esta logica para dar la opcion de cargar str y int en la otra funcion que solo recibe int
    lista = []
    for _ in range(cantidad):
        dato = input(mensaje)
        lista += [dato]
    return lista


def calcular_largo(lista:list)->list:
    lista_vacia = []
    for i in range(medir_coleccion(lista)):
        lista_vacia += [medir_coleccion(lista[i])]

    return lista_vacia
# cargar_nombres = cargar_lista_con_str(5, "Ingrese un nombre")
# elementos_medidos = calcular_largo(cargar_nombres)
# minimo = identificar_menor_entero_de_lista(elementos_medidos)
# indice_del_minimo = identificar_posicion(elementos_medidos, minimo)
# print(f"El nombre mas corto es {cargar_nombres[indice_del_minimo]}")


# 15)
def contar_apariciones_en_lista(lista:list,valor:int)->int:
    contador = 0
    for elemento in lista:
        if valor == elemento:
            contador += 1
    return contador
# lista_cargada = cargar_lista_con_enteros(5, "Ingrese numero: ")
# mayor_de_lista = identificar_mayor_entero_de_lista(lista_cargada)
# cantidad_apariciones_mayor = contar_apariciones_en_lista(lista_cargada,mayor_de_lista)
# print(f"El numero maximo es: {mayor_de_lista}, y la cantidad de veces que aparece es: {cantidad_apariciones_mayor}")


# 16)
def construir_listas_paralelas(cantidad:int, lista_edades:list, lista_nombres:list, mensaje_nombre:str, mensaje_edad:str)->None:
    """
    """
    lista_nombres = []
    lista_edades = []

    for _ in range(cantidad):
        nombre = input(mensaje_nombre)
        edad = int(input(mensaje_edad))
        lista_nombres += [nombre]
        lista_edades += [edad]

def mostrar_mayores_edad(lista_nom:list, lista_edad:list, mayor_edad:int=18)->None:
    """
    """
    print(f"Personas mayores a {mayor_edad}: ")
    for i in range(len(lista_edad)):
        if lista_edad[i] >= mayor_edad:
            print(f"{lista_nom[i]}")
# lista_nombres = []
# lista_edades = []
# construir_listas_paralelas(lista_nombres, lista_edades, 5, "Ingrese nombre: ", "Ingrese edad: ")
# mostrar_mayores_edad(lista_nombres, lista_edades)


# 17)
def construir_listas_paralelas(lista_cadenas:list, lista_numeros:list, cantidad:int, mensaje_producto:str, mensaje_precio:str)->None:
    """
    """
    lista_cadenas = []
    lista_numeros = []

    for _ in range(cantidad):
        lista_cadenas += [input(mensaje_producto)]
        lista_numeros += [int(input(mensaje_precio))]
lista_precios = []
lista_productos = []  

construir_listas_paralelas(lista_productos, lista_precios, 5, "Ingrese producto: ", "Ingrese precio: ")

def calcular_cantidad_precios_mayores_primer_producto(lista_enteros:list)->int:
    """
    """
    primer_elemento = None
    contador = 0
    for i in range(len(lista_enteros)):
        if i == 0:
            primer_elemento = lista_enteros[i]
        else:
            if lista_enteros[i] > primer_elemento:
                contador += 1
    return contador

calculo = calcular_cantidad_precios_mayores_primer_producto(lista_precios)