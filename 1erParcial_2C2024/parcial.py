import random
from MisFunciones import *

# Variables necesarias para acceder a ciertos puntos
numero_seleccionado_en_A = None
lista_mayusculas = None


while True:
    opcion_seleccionada = generar_menu(["Ingresar numero", "Generar lista", 
    "Mostrar lista", "Ingresar una letra", "Ordenar (ASC o DESC)", 
    "Ingresar tamaño de matriz", "Generar matriz", "Mostrar matriz", "Salir"], 9)
    
    match opcion_seleccionada:
        case "A":
            numero_seleccionado_en_A = solicitar_y_validar_numero_en_rango(
                "Ingrese un número entero entre 3 y 15: ", minimo=3, maximo=15
                )
        case "B":
            if numero_seleccionado_en_A != None:

                lista_mayusculas = generar_lista_aleatoria_letras_mayusculas(
                        cantidad_elementos=numero_seleccionado_en_A,
                        minimo=65, maximo=90
                    )
                print("LISTA GENERADA CORRECTAMENTE")
            elif numero_seleccionado_en_A == None:

                print("[REQUERIDO] Antes debe ingresar un número con la opción A")        
        case "C":
            if lista_mayusculas != None:
                print("Lista de letras mayúsculas generadas: ")
                mostrar_lista(lista_mayusculas)
            elif lista_mayusculas == None:
                print("------------------------------------------------------------------")
                print(f"[REQUERIDO] Antes debe generar la lista con la opcion B")
        case "D":
            if lista_mayusculas != None:
                letra_seleccionada = solicitar_y_validar_cadena_y_longitud(
                    "Ingrese UNA sola letra(A-Z): ", 
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1
                )
                lista_indices = buscar_elemento_en_lista(lista_mayusculas, letra_seleccionada)
                if lista_indices != None:
                    print(f"\n\n")
                    print("------------------------------------------------------------------")
                    print("La letra se encuentra en la lista, en la/s posición/es: ")
                    mostrar_lista(lista_indices)
                elif lista_indices == None:
                    print(f"\n\n")
                    print("------------------------------------------------------------------")
                    print("La letra no se encuentra dentro de la lista generada en B. ")
            elif lista_mayusculas == None:
                print("------------------------------------------------------------------")
                print(f"[REQUERIDO] Antes debe generar la lista con la opcion B")
        case "E":
            pass
        case "F":
            pass
        case "G":
            pass
        case "H":
            pass
        case "I":
            break
