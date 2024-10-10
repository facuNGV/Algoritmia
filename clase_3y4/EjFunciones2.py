


# 1) Desarrollar una función que determine si un número entero es par o impar. Debe recibir un número por parámetro y devolver True en caso de que sea par, de lo contrario devolverá False.
def determinar_par_impar(numero:int)->bool:
    """
    Esta función es capaz de determinar si un número es par o impar.
    Recibe: Un número
    Retorna: Verdadero en caso de que el numero sea par o Falso caso
    contrario
    """
    bandera_par = False
    if numero % 2 == 0:
        bandera_par = True
    else:
        bandera_par = False
    return bandera_par


# 2) Desarrollar una función que permita validar un número entero. Deberá recibir por parámetro el número a validar, y dos números que representan el rango mínimo y máximo permitido. Devolverá True en caso de ser válido, False de lo contrario.
def validar_numero_entero_en_rango(numero:int, minimo:int, maximo:int)->bool:
    """
    Esta función valida si un determinado numero se encuentra dentro de un 
    rango determinado
    Recibe: Un numero, un determinado rango numérico
    Retorna: True en caso de que el numero se encuentre dentro del rango
    False caso contrario o None caso de que no se haya ingresado un numero
    """
    retorno = None

    if type(numero) == int and type(minimo) == int and type(maximo) == int:
        if numero >= minimo and numero <= maximo: 
            retorno = True
        else:
            retorno = False
    return retorno


# 3) Desarrollar una función que se encargue de solicitar un número entero al usuario, validarlo (reutilizando la función del punto anterior) y retornar el número validado y transformado a entero. Deberá recibir por parámetro un mensaje que se le mostrará al usuario y los rangos de validación.
def verificador_entero(string:str)->bool:
    '''
    Esta función determina si todos los caracteres en una cadena son números o no.
    Recibe: Una cadena
    Retorna: Verdadero si el dato es un número, falso si no lo es
    '''
    retorno = True
    for digito in string:
        if ord(digito) < 48 or ord(digito) > 57:
            retorno = False
            break

    return retorno


def solicitar_numero_entero(mensaje:str, minimo:int, maximo:int)->int:
    """
    Esta función pide un numero al usuario y valida que se encuentre
    dentro de un rango numérico determinado
    Recibe: Un mensaje que se imprimira al usuario, un rango numérico
    Retorna: El mismo número validado
    """
    bandera = False # La inicializamos en False para forzarla a entrar en el siguiente While

    while bandera == False:
        numero = input(mensaje)
        bandera = verificador_entero(numero) # Función para verificar si se puede castear a entero, devuelve True si se puede
    numero = int(numero) # Se castea luego de verificar

    while validar_numero_entero_en_rango(numero, minimo, maximo) != True:
        bandera = False
        while bandera == False:
            numero = input(mensaje)
            bandera = verificador_entero(numero) 
        numero = int(numero) # Se castea luego de verificar
        # numero = int(input(mensaje))

    return numero


# 4) Desarrollar una función que se encargue de solicitar una cadena de caracteres al usuario, validarla y retornar la misma. Deberá recibir como parámetro un mensaje para indicarle al usuario y 1, 2 o 3 cadenas de caracteres que representarán las opciones válidas de ingreso.
def validar_cadena(
        mensaje:str, ejemplo_1:str, ejemplo_2:str=None, ejemplo_3:str=None,
        )->str:
    """
    Esta función pide al usuario que ingrese una cadena dentro de unas opciones
    válidas determinadas y valida que el usuario ingrese un dato correcto.
    Recibe: El mensaje que se le quiere imprimir al usuario y las opciones
    posibles que el usuario puede elegir.
    Retorna: El dato elegido por el usuario una vez validado.
    """
    cadena = input(mensaje)
    while cadena == "" or (
        cadena != ejemplo_1 and cadena != ejemplo_2 and cadena != ejemplo_3
        ):
        cadena = input(mensaje)
    return cadena


# 5) Desarrollar una función que se encargue de medir el largo de una cadena de caracteres, deberá recibir por parámetro la cadena de caracteres a evaluar y devolverá un número entero representando la longitud de la cadena recibida.
def medir_cadena(cadena:str)->int:
    contador = 0
    for _ in cadena:
        contador += 1
    return contador


# 6) Desarrollar una función que determine si un número que recibirá por parámetro es primo. Si es primo deberá devolver un True, de lo contrario False.
def determinar_primo(numero:int)->bool:

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


# 7)Desarrollar una función que recibirá un número entero por parámetro, y devolverá el resultado del factorial de ese número.
def calcular_factorial(numero:int)->int:

    acumulador = 1

    for i in range(numero, 0, -1):
        acumulador *= i
    return acumulador


# 8)Desarrollar una función que reciba un carácter y determine si ese carácter está comprendido entre a…z o A…Z, en caso afirmativo devolverá True, de lo contrario False.
def verificar_caracter_abecedario(caracter:str)->bool:
    """
    Esta función determina si un caracter se encuentra dentro del abecedario
    Recibe: Un caracter
    Retorna: Verdadero si se encuentra en el abecedario, caso contrario: Falso.
    """
    if (ord(caracter) >= 65 and ord(caracter) <= 90) or (ord(caracter) >= 97 and ord(caracter) <= 122):
        return True
    else:
        return False


# 9)Desarrollar una función que reciba un carácter y determine si ese carácter está comprendido entre 0…9, devolverá un valor boolean indicando si el carácter recibido es numérico o no.
def determinar_caracter_numerico(caracter:str)->bool:
    """
    Esta función determina si un caracter es numerico o no
    Recibe: un caracter
    Retorna: Verdadero si es numero, caso contrario: Falso
    """
    return verificador_entero(caracter)


# 10) Desarrollar una función que verifique el DNI de una persona, la misma recibirá una cadena de caracteres (se asume que solamente contiene caracteres numéricos). Si la cantidad de caracteres es menor a 6 o mayor a 8, retornara False. Si la cantidad de caracteres está comprendida entre 6 y 8 devolverá True.
def verificar_dni(cadena:str)->bool:
    """
    Esta función asumiendo que se le pasan caracteres numéricos determina
    si tiene el formato de un Documento de Identidad Nacional
    Recibe: 
    Retorna: 
    """
    cadena_medidad = medir_cadena(cadena)
    bandera = False
    if cadena_medidad > 5 and cadena_medidad < 9:
        bandera = True
    return bandera


# 11) Desarrollar una función que complete el número de DNI de una persona. Recibirá una cadena de caracteres (se asume que solamente contiene caracteres numéricos), deberá medirla y completar con ceros a la izquierda hasta llegar a un total de 8 caracteres, y devolviendo la cadena resultante. Ej: Se ingresa “123456”, y devolverá “00123456”.
#El profe la hizo más genérica de lo que pedía el ejercicio.
def rellenar_cadena(mensaje:str, minimo_digitos:int=8, relleno:str="0")->str:
    
    cadena = input(mensaje)

    cantidad_a_rellenar = minimo_digitos - medir_cadena(cadena)
    cadena_a_rellenar = ""

    for _ in range(cantidad_a_rellenar):
        cadena_a_rellenar += relleno
    return cadena_a_rellenar + cadena


#12. Desarrollar una función que transforme una cadena de caracteres numérica a su equivalente en letras.
#Recibirá por parámetro la cadena a transformar y devolverá el resultado en letras. Ej: “987” ->
#"novecientos ochenta y siete". Como máximo tomar el número más grande de 3 dígitos

def pasar_unidades(numero:str)->str:
    resultado = ""

    if numero == "1":
        resultado = "uno"
    elif numero == "2":
        resultado = "dos"
    elif numero == "3":
        resultado = "tres"
    elif numero == "4":
        resultado = "cuatro"
    elif numero == "5":
        resultado = "cinco"
    elif numero == "6":
        resultado = "seis"
    elif numero == "7":
        resultado = "siete"
    elif numero == "8":
        resultado = "ocho"
    elif numero == "9":
        resultado = "nueve"
    else:
        resultado = "cero"
    
    return resultado

def pasar_decenas(numero:str, unidad:str="0")->str:
    resultado = ""

    if numero == "1":
        resultado = "diez"
    elif numero == "2":
        resultado = "veinte"
    elif numero == "3":
        resultado = "treinta"
    elif numero == "4":
        resultado = "cuarenta"
    elif numero == "5":
        resultado = "cincuenta"
    elif numero == "6":
        resultado = "sesenta"
    elif numero == "7":
        resultado = "setenta"
    elif numero == "8":
        resultado = "ochenta"
    elif numero == "9":
        resultado = "noventa"
    
    return resultado

def pasar_centenas(numero:str, redondo:bool=False)->str:
    resultado = ""

    match numero:
        case "1":
            resultado = "ciento"
        case "2":
            resultado = "doscientos"
        case "3":
            resultado = "trescientos"
        case "4":
            resultado = "cuatrocientos"
        case "5":
            resultado = "quinientos"
        case "6":
            resultado = "seiscientos"
        case "7":
            resultado = "setecientos"
        case "8":
            resultado = "ochocientos"
        case "9":
            resultado = "novecientos"
        
    if redondo == True and numero == "1":
        resultado = "cien"
    
    return resultado

def determinar_nombre_numero(cadena:str)->str:
    largo_cadena = medir_cadena(cadena)
    cadena = int(cadena)

    centena = str(cadena//100)
    cadena = cadena % 100
    decena = str(cadena //10)
    unidad = str(cadena % 10)

    match largo_cadena:
        case 1:
            resultado = pasar_unidades(unidad)
        case 2:
            resultado = pasar_decenas(decena)
            if unidad != "0":
                resultado = resultado + " y " + pasar_unidades(unidad)
        case 3:
            if decena == "0":
                if unidad == "0":
                    resultado = pasar_centenas(centena, True)
            else:
                resultado = pasar_centenas(centena)
                resultado = resultado + " " + pasar_decenas(decena)
                if unidad != "0":
                    resultado = resultado + " y " + pasar_unidades(unidad)

    return resultado

    