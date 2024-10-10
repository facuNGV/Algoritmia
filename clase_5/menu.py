
def menu(
        opcion1:str, opcion2:str="", opcion3:str="", opcion4:str="", opcion5:str=""
        , opcion6:str="", opcion7:str="", opcion8:str="", opcion9:str="", opcion10:str="" 
         ):
    pass
    menu = f"""A) {opcion1}
B) {opcion2}
D) {opcion3}
F) {opcion4}
G) {opcion5}
H) {opcion6}
I) {opcion7}
J) {opcion8}
K) {opcion9}
L) {opcion10}
"""
    
    return menu
    

print(menu("pepe"))