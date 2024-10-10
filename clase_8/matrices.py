# mi_matriz = [[1, 2, 3, 4], 
#              [10, 20, 30, 40]]

# otra_matriz = [["a","b","c"],
#                ["x","y","z"]]

def mostrar_matriz(matriz:list)->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("")

def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial)->list:
    matriz=[]
    for _ in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz
# mi_matriz = inicializar_matriz(3, 4, 0)
# mostrar_matriz(mi_matriz)

def cargar_matriz_secuencialmente(matriz:list):
    # Le pido al usuario los datos de la matriz
    # como es secuencial debo controlar que 
    # ingrese todos los datos
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Fila {i} columna {j}"))

def cargar_matriz_aleatoriamente(matriz:list):
    seguir = "S"
    while seguir == "S":
        fila = int(input("Indice de la fila: "))
        columna = int(input("Indice de la columna: "))
        dato = int(input("Ingrese el elemento a cargar: "))
        matriz[fila][columna] = dato
        seguir = input("¿Desea seguir cargando elementos? S/N: ")

def buscar_coordenadas(matriz:list, valor):
    lista_coordenadas = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                lista_coordenadas = [i, j]
    return lista_coordenadas
# Ojo, que devuelve una lista de la manera que
# no se debe mostrarla
# print(buscar_coordenadas(otra_matriz, "z"))
