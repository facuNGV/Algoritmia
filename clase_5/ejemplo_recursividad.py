
"""
Observaciones:
El parámetro debe ir cambiando de manera que en determinado momento cumpla
una determinada condición para que el código vaya por una secuencia donde
ya no se llame a la función. El retorno va a ir cambiando también y es lo
que vamos a obtener finalmente en el primer llamado a la función.

"""

def calcular_factorial(numero:int)->int:  #5
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1) # 5 - 1 
        return resultado

def calcular_factorial(numero:int)->int:  #4
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1) # 4 - 1
        return resultado

def calcular_factorial(numero:int)->int:  #3
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1) # 3 - 1
        return resultado

def calcular_factorial(numero:int)->int:  #2
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1) # 2 - 1
        return resultado

def calcular_factorial(numero:int)->int:  #1
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1) # 1 - 1
        return resultado

def calcular_factorial(numero:int)->int:  #0
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1)
        return resultado

