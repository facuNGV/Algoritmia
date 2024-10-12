# 1
# def ordenar_lista(lista:list, criterio:str = "asc")-> bool:
#     """
#     """
#     bandera = False

#     if criterio == "asc":
#         for i in range(len(lista)-1):
#             for j in range(i+1, len(lista)):
#                 if lista[i] > lista[j]:
#                     aux = lista[j]
#                     lista[j] = lista[i]
#                     lista[i] = aux
#                     bandera = True

#     elif criterio == "desc":
#         for i in range(len(lista)-1):
#             for j in range(i+1, len(lista)):
#                 if lista[i] < lista[j]:
#                     aux = lista[j]
#                     lista[j] = lista[i]
#                     lista[i] = aux
#                     bandera = True
                    
#     return bandera

def ordenar_lista(lista:list, criterio:str = "asc")-> bool:
    """
    """
    bandera = False

    
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if (criterio == "asc" and lista[i] > lista[j]) or (criterio == "desc" and lista[i] < lista[j]):
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
                bandera = True

    return bandera

# 2
nombres = ["lautaro", "tomas", "nelson", "carlos", "agustin"]
apellidos = ["veiga", "gonzales", "vega","perez", "lopez"]
edades = [20, 30 , 25 , 18 , 50]

def swapear(lista:list, indice_a=int, indice_b=int)->bool:
        retorno = False
        if len(lista) > 1 and indice_a < len(lista) and indice_b < len(lista):
            aux = lista[indice_a]
            lista[indice_a] = lista[indice_b]
            lista[indice_b] = aux
            retorno = True
        return retorno
    

def ordenar_listas_paralelas(lista_principal:list, lista_a:list, lista_b:list, criterio:str)->bool:
    """
    Ordena la LISTA PRINCIPAL segun un criterio, si vamos a ordenar por edad
    hay que pasarle la lista de edades como primer parametro
    """
    bandera = False
    for i in range(len(lista_principal)-1):
        for j in range(i+1, len(lista_principal)):
            if (criterio == "asc" and lista_principal[i] > lista_principal[j]) or (criterio == "desc" and lista_principal[i] < lista_principal[j]):
                swapear(lista_principal, i, j)
                swapear(lista_a, i, j)
                swapear(lista_b, i, j)
                bandera = True
    return bandera

print(nombres)
print(apellidos)
print(edades)

ordenar_listas_paralelas(edades, nombres, apellidos, "asc")
print("------------------------------------------------")
print(nombres)
print(apellidos)
print(edades)

3
def ordenar_listas_dobles_criterio(lista_principal: list, lista_secundaria: list, criterio: str = "asc") ->bool:
    """
    
    """
    bandera = False
    for i in range(len(lista_principal) - 1):
        for j in range(i + 1, len(lista_principal)):
            if (criterio == "asc" and lista_principal[i] > lista_principal[j]) or (criterio == "desc" and lista_principal[i] < lista_principal[j]):
                swapear(lista_principal, i, j)
                swapear(lista_secundaria, i, j)
                bandera = True
            elif lista_principal[i] == lista_principal[j] and (criterio == "asc" and lista_secundaria[i] > lista_secundaria[j]) or (criterio == "desc" and lista_secundaria[i] < lista_secundaria[j]):
                swapear(lista_secundaria, i, j)
                bandera = True
    return bandera

lista_a = [22, 54, 22, 18]
lista_b = ["damian", "cristian", "bastian", "albo"]
print(lista_a)
print(lista_b)
print("--------------------")
ordenar_listas_dobles_criterio(lista_a, lista_b, "desc")
print(lista_a)
print(lista_b)

4
matriz = [[4,2,6],
          [3,1,7],
          [5,8,10],
          [9,0,-1]]


def ordenar_matriz(matriz:list,criterio:str="asc")->None:
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            for i in range(len(matriz)):
                for j in range(len(matriz[0])):
                    if (criterio == "asc" and matriz[fila][columna] < matriz[i][j]) or (criterio == "desc" and matriz[fila][columna] > matriz[i][j]):
                        aux = matriz[fila][columna]
                        matriz[fila][columna] = matriz[i][j]
                        matriz[i][j] = aux


# 4) Desarrollar una funcion que reciba una matriz y la ordene de acuerdo al criterio recibido
# por parametro. Devolverá un booleano indicando si pudo ordenar los elementos o no.

mi_matriz = [[4, 2, 6],
             [3, 1, 7],
             [10, 8, 5],
             [9, 0, -1]]


def imprimir_matriz(matriz:list)->None:
    for i in range(len(matriz)): # 4
        for j in range(len(matriz[i])): # 3
            print(matriz[i][j], end=" ")
        print("")

def convertir_matriz_a_lista(matriz:list)->list:
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista += [matriz[i][j]]
    return lista

def ordenar_matriz_con_lista_ordenada(lista_ordenada:list, matriz_desordenada:list)->bool:
    bandera = False
    contador = 0
    for i in range(len(matriz_desordenada)): # 4
        for j in range(len(matriz_desordenada[i])): # 3
            matriz_desordenada[i][j] = lista_ordenada[contador]
            contador += 1
            bandera = True
    return bandera
 
                
def ordenar_lista(lista:list, criterio:str = "asc")->bool:
    flag = False
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if (lista[i] > lista[j] and criterio == "asc") or (lista[i] < lista[j] and criterio == "desc"):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                flag = True
    return flag

imprimir_matriz(mi_matriz)
lista_a_ordenar = convertir_matriz_a_lista(mi_matriz)
print("------------------")
print("Matriz desglosada: ")
print(lista_a_ordenar)
ordenar_lista(lista_a_ordenar)
print(lista_a_ordenar)
print("------------------")
ordenar_matriz_con_lista_ordenada(lista_a_ordenar, mi_matriz)
imprimir_matriz(mi_matriz)
print('------------------')