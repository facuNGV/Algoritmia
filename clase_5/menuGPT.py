

def generar_menu(opciones:list, cantidad:int)->None:
    """
    """
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if cantidad > len(opciones):
        print("Cantidad de opciones es mayor que las opciones disponibles.")
        return

    for i in range(cantidad):
        letra = letras[i]
        if i < len(opciones):
            print(f"{letra}) {opciones[i]}")
        else:
            print(f"{letra})")


opciones = ["pepe", "juan", "maria", "pedro", "lucas"]
cantidad = 5
generar_menu(opciones, cantidad)

