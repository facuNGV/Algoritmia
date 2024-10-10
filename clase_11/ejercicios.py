
"""
1)Desarrollar una funcion que reciba una lista de cadenas y devuelva otra lista con las mismas cadenas ordenadas por su largo de menor a mayor.
2)Desarrollar una funcion que reciba una cadena de caracteres, suprima los caracteres repetidos y devuelva la cadena resultante.
3)Desarrollar una funcion que reciba una matriz (sopa de letras) y una cadena de caracteres, si la cadena de caracteres existe en la matriz ya sea horizontal o verticalmente, devolvera True, de lo contrario False.
4)Desarrollar una función que reciba como parámetro una cadena y determine cuántas palabras contiene. La función deberá retornar un entero indicando el número de palabras
5)Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
Por ej: cadena = “murcielaguito”
"""

# 1)Desarrollar una funcion que reciba una lista de cadenas y devuelva otra lista con las mismas cadenas ordenadas por su largo de menor a mayor.
lista = ["Federico", "Manuel", "Luis", "Nahuel"]
def ordenar_listas_por_largo(lista:list, criterio:str)-> list:
    """
    """
    lista_ordenada = lista[:]
    for i in range(len(lista_ordenada) - 1):
        for j in range(i + 1, len(lista_ordenada)):
            if (len(lista_ordenada[i]) > len(lista_ordenada[j]) and criterio == "ascendente") or (len(lista_ordenada[i]) < len(lista_ordenada[j]) and criterio == "descendente"):
                aux = lista_ordenada[i]
                lista_ordenada[i] = lista_ordenada[j]
                lista_ordenada[j] = aux
    return lista_ordenada
# print(lista)
# print(ordenar_listas_por_largo(lista, "descendente"))
# print(lista)


# 2)Desarrollar una funcion que reciba una cadena de caracteres, suprima los caracteres repetidos y devuelva la cadena resultante.
def quitar_repetido(cadena:str) -> str:
    """
    """
    # Hooola (Hola)
    acumulador = ""
    for i in range(len(cadena)-1):
        if cadena[i] != cadena[i+1]:
            acumulador += cadena[i]
    acumulador += cadena[len(cadena)-1]
    return acumulador
# print(quitar_repetido("Hooolo"))


# 3)Desarrollar una funcion que reciba una matriz (sopa de letras) y una cadena de caracteres, si la cadena de caracteres existe en la matriz ya sea horizontal o verticalmente, devolvera True, de lo contrario False.
sopa_de_letras = [["s","o","p","f"]
                  ["o","f","w","r"]
                  ["s","o","p","a"]
                  ["a","s","r","n"]]

def encontrar_palabra(matriz:list, palabra:str)->bool:
    for i in range(len(matriz)):
        for j in range(len(matriz[i]))





