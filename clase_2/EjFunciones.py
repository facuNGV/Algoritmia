

# 1) Desarrollar una función que reciba como parámetros fecha actual y fecha de nacimiento; y retorne la edad.
def mostrar_edad(fecha_nacimiento:str, fecha_actual:str)->int:
    '''
    Esta función..
    Recibe:
    Retorna:
    '''
    dia_nacimiento = cortar_cadena(fecha_nacimiento, 1, 2)
    mes_nacimiento = cortar_cadena(fecha_nacimiento, 4, 5)
    año_nacimiento = cortar_cadena(fecha_nacimiento, 7, 10)

    dia_actual = cortar_cadena(fecha_actual, 1, 2)
    mes_actual = cortar_cadena(fecha_actual, 4, 5)
    año_actual = cortar_cadena(fecha_actual, 7, 10)

    edad = int(año_actual) - int(año_nacimiento)

    if (mes_actual < mes_nacimiento) or (mes_actual == mes_nacimiento and dia_actual < dia_nacimiento):
        edad -= 1

    return edad


# 2) Desarrollar una función que reciba una patente que tendrá tres letras y tres números o tres números y tres
# letras. Deberá retornar auto o moto, si la patente es tres letras y tres números o tres números y tres letras
# respectivamente.
def cortar_cadena(cadena:str, desde:int, hasta:int)->str:
    contador = 1
    resultado = ""
    for letra in cadena:
        if contador >= desde and contador <= hasta:
            resultado += letra 
        contador += 1
    
    return resultado

def determinar_vehiculo(patente:str)->str:
    '''
    funcion que recibe una patente como parametro 
    retorna tipo de vehiculo
    '''
    letra1 = cortar_cadena(patente, 1, 1)
    
    if ord(letra1) > 47 and ord(letra1) < 58:
        vehiculo = "Moto"
    else:
        vehiculo = "Auto"

    return vehiculo


"""
3) Desarrollar una función que reciba como parametros numero de DNI y
[MASCULINO|FEMENINO|EMPRESA]. Deberá retornar el CUIL/CUIT formado por:
CUIL/T: Son 11 números en total:
XY – 12345678 – Z
XY: Indican el tipo (Masculino, Femenino o una empresa)
12345678: Número de DNI
Z: Código Verificador
Algoritmo: Se determina XY con las siguientes reglas:
Masculino: 20
Femenio: 27
Empresa: 30
Se multiplica XY 12345678 por un número de forma separada:
X * 5
Y * 4
1 * 3
2 * 2
3 * 7
4 * 6
5 * 5
6 * 4
7 * 3
8 * 2
Se suman dichos resultados. El resultado obtenido se divide por 11. De esa división se obtiene un Resto que
determina Z.
Si el resto es 0 = Entonces Z = 0.
Si el resto es 1 = Entonces se aplica la siguiente regla:
*Si es hombre: Z = 9 y XY pasa a ser 23
*Si es mujer: Z = 4 y XY pasa a ser 23
Caso contrario Z pasa a ser (11 - Resto).
"""

def generar_cuil(dni:int, tipo:str) -> str:
    '''
    '''
    match tipo:
        case "masculino":
            xy = "20"
        case "femenino":
            xy = "27"
        case "empresa":
            xy = "30"
            
    documento_aux = xy + str(dni)
    mult = 5
    acumulador = 0

    for digito in documento_aux:
        acumulador += (int(digito) * mult)
        mult -= 1
        if mult == 1:
            mult = 7

    resto = acumulador % 11

    if resto == 0:
        digito_verificador = resto
    elif resto == 1:
        if tipo == "masculino":
            digito_verificador = 9
            xy = 23
        elif tipo == "femenino":
            digito_verificador = 4
            xy = 23
        else:
            digito_verificador = str(11-resto)
    else:
        digito_verificador = 11 - resto
        
    cuil = f"{xy}-{dni}-{digito_verificador}"

    return cuil