apellidos =         ["Perez", "Fernandez", "Gomez"]
antiguedad =        [15,5,20]
legajos =           [435,250,673]
codigo_sector_emp = [1,2,1]

id_sectores =   [1,2]
sectores =      ["Sistemas", "RRHH"]

print(f'{"Apellido":15}{"Antiguedad":12}{"Legajo":8}{"Sector":4}')
print("---------------------------------------------------")
for i in range(len(apellidos)): # 3
    for j in range(len(sectores)): # 2
        #  1, 2, 1  ==  1, 2
        if codigo_sector_emp[i] == id_sectores[j]:
            print(f"{apellidos[i]:10}{antiguedad[i]:12}{legajos[i]:9}    {sectores[j]:8}")
