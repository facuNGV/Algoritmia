import random
from MisFunciones import *
def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any=0) -> list:
    """
    Esta función se encarga de crear una matriz vacía
        Recibe:
            cantidad_filas (int): representa las filas que va a tener la matriz
            cantidad_columans (int): representa las columnas que va a tener la matriz

        Devuelve:
            matriz (list): la matriz creada a través de los parámetros
    """
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]

    return matriz

def llenar_matriz_aleatoriamente(matriz_vacia:list, desde:int, hasta:int)->None:
    for i in range(len(matriz_vacia)):
        for j in range(len(matriz_vacia[i])):
            matriz_vacia[i][j] = str(random.randint(desde,hasta))


matriz = crear_matriz(3,7,0)
llenar_matriz_aleatoriamente(matriz, 1, 9)
mostrar_matriz(matriz)