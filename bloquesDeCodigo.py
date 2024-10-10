# Limpiar la consola automaticamente
class example:
    import os
    os.system("cls")

# Verificar si un determinado string es un numero
class example:
    def verificador_numeros(dato:str)->bool:
        '''
        Esta funcion determina si el dato ingresado se trata de un numero o no
        Recibe: un dato cualquiera de tipo string
        Retorna: verdadero si el dato es un numero, falso si no lo es
        '''
        # Verificar si se ingreso algo o no se ingreso nada
        if not dato:
            return False
        # Variables para controlar mas adelante si tiene coma y digitos
        tiene_coma = False
        tiene_digitos = False
        # variable que ira aumentando luego de cada iteración, para saber en qué vuelta va el ciclo
        pos = 0
        # Recorrer cada carácter en la cadena
        for char in dato:
            if char == '-':
                # Si entró acá es porque hay un signo negativo, acto seguido pregunto si ese signo negativo esta primero o no
                if pos != 0:
                    # Si entra aca: el signo "-" no está primero, no es un numero, asi que termina la funcion
                    return False 
            elif char == ',':
                # Verificar si ya hay una coma decimal
                if tiene_coma:
                    # Si habia: termina la funcion, no puede haber 2 comas.
                    return False
                tiene_coma = True
            elif char in "0123456789":
                tiene_digitos = True
            else:
                return False

            # Incrementar contador de posición
            pos += 1

        return tiene_digitos 

#  Validacion string
class Example:
    def validar_cadena(
            mensaje:str, ejemplo_1:str, ejemplo_2:str=None, ejemplo_3:str=None,
            ejemplo_4:str=None, ejemplo_5:str=None, ejemplo_6:str=None,
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
            cadena != ejemplo_1 and cadena != ejemplo_2 and cadena != ejemplo_3 and
            cadena != ejemplo_4 and cadena != ejemplo_5 and cadena != ejemplo_6
            ):
            cadena = input(mensaje)
        return cadena

# Validacion numero, este es muy especifico depende el ejercicio
class Example:
    variable = input("Por favor, ingrese su nombre: ")
    while variable > 0:
        variable = input("[ERROR] Por favor, ingrese su nombre: ")

#Buscar mayor entre 3 datos ya dados contemplando igualdades
class Example:

    masculino_ovni_humanoide = 0
    femenino_ovni_humanoide = 0
    otro_ovni_humanoide = 0
    if masculino_ovni_humanoide == femenino_ovni_humanoide and masculino_ovni_humanoide == otro_ovni_humanoide:
        print("Los tres generos registraron \"Figura humanoide\" la misma cantidad de veces")
    elif masculino_ovni_humanoide == femenino_ovni_humanoide:
        if masculino_ovni_humanoide > otro_ovni_humanoide:
            genero_frecuente_humanoide = masculino_ovni_humanoide
        else:
            genero_frecuente_humanoide = otro_ovni_humanoide
    elif femenino_ovni_humanoide == otro_ovni_humanoide:
        if femenino_ovni_humanoide > masculino_ovni_humanoide:
            genero_frecuente_humanoide = femenino_ovni_humanoide
        else:
            genero_frecuente_humanoide = masculino_ovni_humanoide
    elif masculino_ovni_humanoide == otro_ovni_humanoide:
        if masculino_ovni_humanoide > femenino_ovni_humanoide:
            genero_frecuente_humanoide = masculino_ovni_humanoide
        else:
            genero_frecuente_humanoide = femenino_ovni_humanoide 
    # Si son todos los numeros diferentes busco el mayor
    if masculino_ovni_humanoide > femenino_ovni_humanoide and masculino_ovni_humanoide > otro_ovni_humanoide:
        genero_frecuente_humanoide = masculino_ovni_humanoide
    elif femenino_ovni_humanoide > masculino_ovni_humanoide and femenino_ovni_humanoide > otro_ovni_humanoide:
        genero_frecuente_humanoide = femenino_ovni_humanoide
    elif otro_ovni_humanoide > masculino_ovni_humanoide and otro_ovni_humanoide > femenino_ovni_humanoide:
        genero_frecuente_humanoide = otro_ovni_humanoide

# Evaluar si un numero es primo con while
class Example:
    numero = int(input("Dame un número: "))
    contador_divisores = 0
    contador_resto_0 = 0
    while contador_divisores < numero:
        contador_divisores += 1
        if numero % contador_divisores == 0:
            contador_resto_0 += 1
    if contador_resto_0 == 2:
        print(f"El numero {numero} es un número primo.")
    else: 
        print(f"El número {numero} no es primo. ")

# Obtener maximos y minimos
class Example:
    contador=0
    bandera_primer_dato = False

    while contador < 9:

        num = int(input("Ingrese un numero: "))
        if bandera_primer_dato == False:
            min_numero = num
            max_numero = num
            bandera_primer_dato = True
        if num < min_numero:
            min_numero = num
        elif num > max_numero:
            max_numero = num

        contador+=1

    print("ejecuciones: ",contador)
    print("el valor min es: ", min_numero)
    print("el valor max es: ", max_numero)

# Obtener maximo
class Example:
    # fuera del bucle
    variable_max = None

    # dentro del bucle
    variable = input("Ingrese un numero: ")
    if variable_max == None or variable > variable_max:
        variable_max = variable

# Obtener minimo
class Example:
    # fuera del bucle
    variable_min = None

    # dentro del bucle
    variable = input("Ingrese un numero: ")
    if variable_min == None or variable < variable_min:
        variable_min = variable

# Acumulador de string
class Example: 

    acumulador_de_nombres_masculinos = ""
    masculino = "masculino"
    femenino = "femenino"
    continuar = 2
    while continuar != 0:
        sexo = input("Ingrese el sexo: ")
        nombre = input("Ingrese nombre: ")
        if sexo == masculino:
            acumulador_de_nombres_masculinos += f"{nombre} "
        continuar = int(input("Ingrese [0] para terminar. Cualquier número para continuar: "))
    print(f"Las personas ingresadas masculinas son: {acumulador_de_nombres_masculinos}")

    #Otro ejemplo
    acumulador_string = ''
    contador = 0
    while contador < 4:
        ingreso_nombre = input('Dame un nombre: ')
        ingreso_edad = int(input('Dame una edad: '))
        ingreso_sexo = input('Sexo: ')
        if ingreso_edad > 17 and ingreso_sexo == 'masculino':
            acumulador_string += f'{ingreso_nombre}\n'
        contador+=1
    print(f'Nombres en el acumulador:\n{acumulador_string}')

# Ejercicio saber cuantos camiones necesito dado un determinado peso de materiales
class Example:

    # En el siguiente acumulador tengo no solo la capacidad del camion
    # sino que acumulo y tengo la capacidad de todos los que se vayan sumando
    variable1 = 3500
    contador_camiones = 1
    kg_materiales = float(input()) #input
    # Comparo constantemente si la cantidad de materiales que me ingresaron
    # superan a capacidad de los camiones que se van sumando
    while kg_materiales > variable1:

        variable1 += 3500
        contador_camiones += 1

    print(f"Se necesitó {contador_camiones} camión/es")

# Funcion para cortar una cadena:
class Example:
    def cortar_cadena(cadena:str, desde:int, hasta:int)->str:
        contador = 1
        resultado = ""
        for letra in cadena:
            if contador >= desde and contador <= hasta:
                resultado += letra
            contador += 1

        return resultado