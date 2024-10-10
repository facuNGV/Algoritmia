"""
La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
contagio, de cada una debe obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
1000 unidades)
4. La marca y el Fabricante.

Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total.
"""

# variables literales
barbijo = "barbijo"
jabon = "jabon"
alcohol = "alcohol"
# variable para buscar el mas caro de los barbijos
barbijo_precio_max = None
# variable para buscar item con mas unidades
item_unidades_max = None
# unidades de jabon total
unidades_jabon_acumulador = 0

for i in range(5):

    tipo_producto = input("Ingrese el tipo de producto(barbijo, jabón o alcohol): ")
    while tipo_producto != barbijo and tipo_producto != jabon and tipo_producto != alcohol:
        tipo_producto = input("Ingrese el tipo de producto(barbijo, jabón o alcohol): ")

    precio_producto = float(input("Ingrese el precio del producto(entre 100 y 300: )"))
    while precio_producto <= 100 or precio_producto >= 300:
        precio_producto = float(input("Ingrese el precio del producto(entre 100 y 300: )"))

    cantidad_unidades = int(input("Ingrese la cantidad de unidades(no debe superar 1000): "))
    while cantidad_unidades <= 0 or cantidad_unidades > 1000:
        cantidad_unidades = int(input("Ingrese la cantidad de unidades(no debe superar 1000): "))
    marca = input("Ingrese la marca del producto: ")
    fabricante = input("Ingrese fabricante del producto: ")

    #Informes

    # A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
    # Variables respuesta: cantidad_unidades_del_barbijo_precio_max, fabricante_del_barbijo_precio_max
    if tipo_producto == barbijo:
        if barbijo_precio_max == None or precio_producto > barbijo_precio_max:
            barbijo_precio_max = precio_producto
            cantidad_unidades_del_barbijo_precio_max = cantidad_unidades
            fabricante_del_barbijo_precio_max = fabricante

    # B. Del ítem con más unidades, el fabricante.
    # Variables respuesta: fabricante_item_unidades_max
    if item_unidades_max == None or cantidad_unidades > item_unidades_max:
        item_unidades_max = cantidad_unidades
        fabricante_item_unidades_max = fabricante

    # C. Cuántas unidades de jabones hay en total.
    # Variables respuesta: unidades_jabon_acumulador
    if tipo_producto == jabon:
        unidades_jabon_acumulador += cantidad_unidades

respuestaA = "A. Del más caro de los barbijos, la cantidad de unidades es de: "
respuestaA += f"{cantidad_unidades_del_barbijo_precio_max} y el fabricante es: "
respuestaA += f"{fabricante_del_barbijo_precio_max}"

respuestaB = "B. Del ítem con más unidades, el fabricante es: "
respuestaB += f"{fabricante_item_unidades_max}"

respuestaC = f"C. Hay {unidades_jabon_acumulador} unidades de jabones en total"

print(f"{respuestaA}\n{respuestaB}\n{respuestaC}")