from data import *
from funciones import *


# # 
# # Programa principal 
# # 

nombre_usuario = input("Ingrese su nombre y apellido: ").lower()
indice_usuario = registro_usuario(nombre_usuario, clientes) # Se almacena la ubicacion final la lista del usuario para facilitar su uso

# Si 'registro_usuario()' retorna error se vuelve a llamar a la funcion y se vuelve a almacenar en 'indice_usuario'
while indice_usuario == "error":
    nombre_usuario = input("Ingrese su nombre y apellido: ").lower()
    indice_usuario = registro_usuario(nombre_usuario, clientes)
    

menu()
opcion = input("Ingrese la opcion: ")

# Se previene maneja el error si el usuario ingresa otro dato o nada
while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "0" :
    print("ERROR: Debe ingresar una de las opciones del menu")
    menu()
    opcion = input("Ingrese la opcion: ")

while opcion != "0":
    if opcion == "1" :
        opcion = cargar_turno(indice_usuario, clientes, profesionales)
    elif opcion == "2" :
        opcion = mostrar_turnos_cliente(indice_usuario, clientes)
    elif opcion == "3" :
        opcion = mostrar_turnos_profesionales(profesionales)