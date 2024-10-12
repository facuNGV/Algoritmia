import random
# indispensable: mostrar lista, pedir dato de usuario, mostrar matriz, las de matrices, las de listas
# tener el menu
'''
    Usuarios
'''
def solicitar_y_validar_numero(mensaje:str)->int|float:
    """
    Esta función pide un dato por consola y valida que su valor sea numérico
    Recibe: El mensaje a imprimir al usuario
    Retorna: El numero validado
    """
    numero = input(mensaje)
    while determinar_numero(numero) == False:
        numero = input(mensaje)
    numero = castear_dato(numero)
    return numero
def solicitar_y_validar_numero_en_rango(mensaje:str, minimo:int, maximo:int)->int:
    """
    Esta función pide un numero al usuario y valida que se encuentre
    dentro de un rango numérico determinado (inclusive)
    Recibe: Un mensaje que se imprimira al usuario, un rango numérico
    Retorna: El mismo número validado y casteado
    """
    numero = input(mensaje)
    while comprobar_numero_dentro_de_rango(numero, minimo, maximo) != True:
        numero = input(mensaje)
    numero = castear_dato(numero)
    return numero
def solicitar_y_validar_cadena_y_longitud(
        mensaje:str, opciones:list|str, longitud:int=None
        )->str:
    """
    Esta función pide al usuario que ingrese una cadena o caracter dentro de una 
    de las opciones válidas determinadas y valida que el usuario ingrese un dato 
    correcto.
    Recibe: El mensaje que se le quiere imprimir al usuario y un iterable con
    las opciones posibles que el usuario puede elegir.
    Retorna: El dato elegido por el usuario una vez validado.
    """
    cadena = input(mensaje)
    if longitud != None:
        while medir_coleccion(cadena) != longitud:
            cadena = input(mensaje)

    while (cadena in opciones) == False:
        cadena = input(mensaje)
    
    return cadena
def generar_menu(opciones:list, cantidad:int):
    """
    """
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if cantidad > len(opciones):
        print("Cantidad de opciones es mayor que las opciones disponibles.")
        return
    
    print("------------------------------------------------------------------")
    for i in range(cantidad):
        letra = letras[i]
        if i < len(opciones):
            print(f"               {letra}) {opciones[i]}")
        else:
            print(f"               {letra})")     
    print("------------------------------------------------------------------")
    opcion_seleccionada = input(f"\nPor favor, seleccione una opción: ")
    print("------------------------------------------------------------------")
    print(f"\n\n")
    return opcion_seleccionada
# Situacional para usar | Listas
def cortar_iterable(iterable:str|list, desde:int, hasta:int)->str|list:
    """
    Esta función recorta un iterable según las posiciones que se le
    pasen por parametro (0, n). Entre esas dos posiciones (inclusive) 
    es que se recortara el iterable. 
    Recibe: El iterable y las posiciones en las que queremos cortar
    Retorna: El iterable recortado
    """
    contador = 0
    if type(iterable) == list:
        resultado = []
        for letra in iterable:
            if contador >= desde and contador <= hasta:
                resultado += [letra]
            contador += 1
    else:
        resultado = ""
        for letra in iterable:
            if contador >= desde and contador <= hasta:
                resultado += letra
            contador += 1

    return resultado
# Situacional para usar
def comprobar_numero_dentro_de_rango(numero:int|float, minimo:int|float, maximo:int|float) -> bool:
    """
    Esta función valida si un determinado numero se encuentra dentro de un 
    rango determinado (inclusive)
    Recibe: Un numero, un determinado rango numérico
    Retorna: True en caso de que el numero se encuentre dentro del rango
    False caso contrario o None caso de que no se haya ingresado un numero
    """
    retorno = None
    if determinar_numero(numero) != False:
        numero = castear_dato(numero)
        if numero >= minimo and numero <= maximo: 
            retorno = True
        else:
            retorno = False
    return retorno
# Situacional para usar
def determinar_numero(dato:str)->bool|str:
        '''
        Esta función determina si el dato ingresado es un número y su tipo.
        Permite la coma o el punto para decimales indistintamente (cuidado en los flaots).
        Recibe: un str cualquiera
        Retorna: el tipo de dato en caso de que sea un número, caso contrario
        devuelve False
        '''
        retorno = False
        # Verificar si se ingreso algo o no se ingreso nada
        if not dato:
            return False
        # Variables para controlar mas adelante si tiene coma y digitos
        tiene_coma = False
        tiene_digitos = False
        # Contador de Iteraciónes
        pos = 0
        # Recorrer cada carácter en la cadena
        for char in dato:
            if char == '-':
                # Si el signo negativo no está primero no es un número
                if pos != 0:
                    return False
            elif char == ',' or char == ".":
                # La coma no puede estar al principio, ni al final, no pueden
                # haber dos y el caracter anterior no puede ser "-"
                if pos == 0 or pos == (len(dato)-1) or tiene_coma == True or caracter_anterior == "-":
                    return False
                tiene_coma = True
            # Todos los demás caracteres deben ser dígitos.
            elif ord(char) >= 48 and ord(char)<= 57:
                tiene_digitos = True
            else:
                return False
            pos += 1
            caracter_anterior = char
        # Determinar que tipo es
        if tiene_digitos == True and tiene_coma == True:
            retorno = "float"
        elif tiene_digitos == True and tiene_coma == False:
            retorno = "int"
        return retorno
# Situacional para usar
def castear_dato(dato:str|int|float)->str|int|float:
    """
    Esta función castea un dato determinado al tipo que le corresponda
    Recibe: un dato
    Retorna: el mismo dato casteado a su tipo correspondiente
    """
    retorno = None
    # determinar_numero devolverá float aunque el decimal tenga un punto (.) o una coma (,)
    # Transformo en un punto (.) independientemente de como este el decimal:
    if determinar_numero(dato) == "float":
        float_coma_string = str(dato)
        float_punto_string = ""
        for digito in float_coma_string:
            if digito == ",":
                float_punto_string += "."
            else:
                float_punto_string += digito
        retorno = float(float_punto_string)
    elif determinar_numero(dato) == "int":
        retorno = int(dato)
    elif type(dato) == str:
        retorno = str(dato)
    elif type(dato) == bool:
        retorno = bool(dato)

    return retorno
# Situacional para usar
def medir_coleccion(coleccion:str|list|int|float)->int:
    """
    Esta función determina de cuantos caracteres esta compuesta una cadena
    Recibe: una cadena cualquiera
    Retorna: el numero de caracteres que compone la cadena
    """
    contador = 0
    for _ in coleccion:
        contador += 1
    return contador
# Matemática
def determinar_primo(numero:int)->bool:
    """
    Esta función determina si un número es primo o no
    Recibe: un numero 
    Retorna: True en caso de ser primo, caso contrario False
    """
    contador_divisores = 0
    contador_resto_0 = 0
    while contador_divisores < numero:
        contador_divisores += 1
        if numero % contador_divisores == 0:
            contador_resto_0 += 1
    if contador_resto_0 == 2:
        return True
    else: 
        return False
# Matemática
def calcular_factorial(numero:int)->int:
    """
    Esta funcion calculara el factorial de un numero 
    Recibe: Un número entero
    Retorna: El factorial de dicho número
    """
    acumulador = 1
    for i in range(numero, 0, -1):
        acumulador *= i
    return acumulador
# Otros
def rellenar_cadena(mensaje:str, minimo_digitos:int=8, elemento_relleno:str="0")->str:
    cadena = input(mensaje)
    cantidad_a_rellenar = minimo_digitos - medir_coleccion(cadena)
    relleno = ""
    for _ in range(cantidad_a_rellenar):
        relleno += elemento_relleno
    return relleno + cadena
# Listas
def append_casero(append_casero_lista:list, elemento:str|int|float|bool|list=None, mensaje:str=None)->None:
    """
    Un elemento solicitado al usuario o pasado por parámetro se añade a una lista
    Recibe: O bien... el elemento por parámetro o bien... el mensaje para 
    solicitar el elemento al usuario. Y la lista que se desea modificar.
    Retorna: None
    """
    if mensaje != None:
        elemento = input(mensaje)
        elemento = castear_dato(elemento)
    append_casero_lista += [elemento]
# Listas
def solicitar_subir_elementos_en_indice(lista:list)->None:
    """
    Esta función pide al usuario índices y elementos determinados y los sube a una lista pasada
    por parámetro. No inserta, por lo que si ya hay un elemento en la posición lo reemplazará.
    Pedirá datos hasta que el usuario lo quiera
    Recibe: La lista a modificar, los mensajes para solicitar los datos al usuario
    Retorna: None 
    """
    mensaje_indice = "¿En que posición desea agregar el elemento?: "
    mensaje_elemento = "Ingrese el elemento a añadir: "
    while True:
        indice_ingresado = solicitar_y_validar_numero_en_rango(mensaje_indice, 0, (len(lista)-1))
        
        elemento_ingresado = input(mensaje_elemento)
        if determinar_numero(elemento_ingresado) == "int":
            elemento_ingresado = int(elemento_ingresado)
        elif determinar_numero(elemento_ingresado) == "float":
            elemento_ingresado = float(elemento_ingresado)
 
        lista[indice_ingresado] = elemento_ingresado

        respuesta = input("Desea seguir ingresando datos? S/N: ")        
        if respuesta == "N":
            break
# here
def buscar_elemento_en_lista(lista:list, dato:int)->list|None:
    coincidencias = []
    for i in range(medir_coleccion(lista)):
        if dato == lista[i]:
            coincidencias += [i]
    if medir_coleccion(coincidencias) == 0:
        coincidencias = None
    return coincidencias
#le agregaria una validacion que me valide si son numeros lo que ingresa el usuario
def pedir_elementos_para_lista(cantidad:int, mensaje:str, tipo:str)->list:
    """
    """
    lista = []
    for _ in range(cantidad):
        dato = input(mensaje)
        if tipo == "int":
            dato = int(dato)
        elif tipo == "float":
            dato = float(dato)
        lista += [dato]
    return lista
def cargar_lista(cantidad:int, mensaje:str, tipo:str)->list:
    """
    """
    lista = []
    for _ in range(cantidad):
        dato = input(mensaje)
        if tipo == "int":
            dato = int(dato)
        elif tipo == "float":
            dato = float(dato)
        lista += [dato]
    return lista
def generar_lista_aleatoria_numeros(cantidad_numeros:int, minimo:int, maximo:int)->list:
    """
    """
    lista_numeros = []
    for _ in range(cantidad_numeros):
        lista_numeros += [random.randint(minimo, maximo)]
    return lista_numeros
def generar_lista_aleatoria_letras_mayusculas(cantidad_elementos:int, minimo:int, maximo:int)->list:
    """
    """
    lista_letras_aleatorias = []
    for _ in range(cantidad_elementos):
        numero_aleatorio = random.randint(minimo, maximo)
        letra = chr(numero_aleatorio)
        lista_letras_aleatorias += [letra]
    return lista_letras_aleatorias
def mostrar_lista(lista:list)->None:
    """
    """
    for elemento in lista:
        if elemento == lista[-1]:
            print(elemento)
        else:
            print(f"{elemento}", end=" , ")

