lista = [6,3,4,1,2,5,-2, 9] # len = 8

print(lista) # PROHIBIDO

# ordenamos Asc     8    -1          ->>> 7 [0,1,2,3,4,5,6]
for i in range(len(lista)-1):
    for j in range(i+1, len(lista)):
 # [6,3,4,1,2,5,-2]   # [3,4,1,2,5,-2,9]
        if lista[i] > lista[j]:
            # Swap
            aux = lista[j]
            lista[j] = lista[i]
            lista[i] = aux


print(lista) # PROHIBIDO