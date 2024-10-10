saludo = "Hola mundo!"

#Slice
# mundo = saludo[ : ]

lista = [2, 3, 4]
print(id(lista), lista)
lista_b = lista[ : ] # Forma de copiar una lista, sin alterarla
print(id(lista_b), lista_b)
lista[1] = 7
print("--------------------------")
print(id(lista), lista)
print(id(lista_b), lista_b)