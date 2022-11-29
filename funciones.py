import re


# Funcion para mostrar el menu
def menu() :
    print("Presione 1 para reservar un nuevo turno")
    print("Presione 2 para ver sus turnos reservados")
    print("Presione 3 para ver los profesionales y su disponibilidad")
    print("0 para salir")

# Funcion para volver al menu o finalizar el programa
def salir() :
    opc = input("Ingrese cualquier letra para volver al menu principal o '0' para cerrar sesion ")
    if opc != "0" :
        menu()
        opc = input("Ingrese la opcion: ")    
    return opc


# Funcion para evaluar que los datos ingresados por el usuario sean letras o espacios y corregir si hay espacios en blanco al incio y al final
def eval_input(dato) :
    dato_limpio = dato.strip()
    lista_filtrada = re.findall("[a-zA-Z\s]", dato_limpio) # Guarda en 'x' una lista con todos los caracteres que son letras o espacios en blanco
    if len(dato) == 0 : # Si el campo esta vacio devuelve que hay error
        print("ERROR: El campo esta vacio. Debe ingresar su nombre y apellido")
        return True
    elif len(lista_filtrada) != len(dato_limpio) : # Si la longitud de la lista es igual a la longitud del string pasado devuelve que hay error
        print("ERROR: Se ha ingresado un caracter invalido. Debe ingresar su nombre y apellido, sin numeros ni caracteres especiales")
        return True
    else : 
        return False
 

# Funcion de "login": pide al usuario nombre y apellido, verifica si existe en la lista de clientes y lo suma o no a la lista.
def registro_usuario(nombre_apellido, lista_clientes) :
    existe = False
    if eval_input(nombre_apellido) :
        return "error"
    for cliente in lista_clientes :
        if cliente[0] == nombre_apellido :
            existe = True 
            index = lista_clientes.index(cliente)
            print("¡Bienvenido " + nombre_apellido + "!")
    if existe == False :
        lista_clientes.append([nombre_apellido, []])
        index = len(lista_clientes) - 1
        print("¡Bienvenido " + nombre_apellido + "!")
    return index


# Funcion para evaluar que no que un cliente no tenga 2 turnos en el mismo horario
def eval_turno_cliente(turno_nuevo, turnos) :
    for turno in turnos :  
        if turno_nuevo[2] == turno[2] and turno_nuevo[3] == turno[3] :
            return False
    return True
    

# Funcion para evaluar que no que un profesional no tenga 2 turnos en el mismo horario
def eval_turno_profesional(turno_nuevo, profesionales) :
    for profesional in profesionales :
        if profesional[0] == turno_nuevo[1] :
            for turno in profesional[2] :  
                if turno_nuevo[2] == turno[0] and turno_nuevo[3] == turno[1] and turno[2] == "reservado" :
                    return False
    return True


# Funcion para cargar un nuevo turno, pide al usuario los siguientes datos: especialidad, nombre del profesional, dia, horario. 
# Verifica que tanto usuario como profesional solicitado no tengan un turno reservado en el mismo horario y modifica el turno en la lista del usuario y del profesional
def cargar_turno(index, lista_clientes, lista_profesionales) :
    turnos_cliente = lista_clientes[index][1]
    servicio = input("Ingrese el servicio: ").lower()
    while eval_input(servicio) :
        servicio = input("Ingrese el servicio: ").lower()
    profesional = input("Ingrese el nombre del profesional: ").lower()
    while eval_input(profesional) :
        profesional = input("Ingrese el nombre del profesional: ").lower()
    dia = input("Ingrese el dia: ").lower()
    while eval_input(dia) :
        dia = input("Ingrese el dia: ").lower()
    horario = input("Ingrese el horario: ")
    while not horario.isdigit() :
        print("ERROR: El dato ingresado no es un numero")
        horario = input("Ingrese el horario: ")
    datos_turno = [servicio, profesional, dia, int(horario)]
    disponibilidad_cliente = eval_turno_cliente(datos_turno, turnos_cliente)
    disponibilidad_profesional = eval_turno_profesional(datos_turno, lista_profesionales)
    if disponibilidad_cliente and disponibilidad_profesional :
        turnos_cliente.append(datos_turno) # Se agrega el nuevo turno a la lista de turnos del usuario
        for profesional in lista_profesionales : # Se cambia el estado del turno del profesional de 'libre' a 'reservado'
            if profesional[0] == datos_turno[1] :
                for turno in profesional[2] :  
                    if datos_turno[2] == turno[0] and datos_turno[3] == turno[1] : 
                        turno[2] = "reservado"
        print("Su turno para " + datos_turno[0] + " con el profesional " + datos_turno[1] + " fue reservado para el dia " + datos_turno[2] + " a las " + str(datos_turno[3]) + "hs")
        opc = input("Ingrese '1' para cargar otro turno, '2' para volver al menu principal o '0' para cerrar sesion: ")
        if opc == "2" :
            menu()
            opc = input("Ingrese la opcion: ")
        return opc
    elif not disponibilidad_cliente : 
        print("Usted ya tiene un turno reservado ese dia y horario")
        opc = input("Ingrese '1' para cargar un turno en otro horario, '2' para volver al menu principal o '0' para cerrar sesion: ")
        if opc == "2" :
            menu()
            opc = input("Ingrese la opcion: ")
        return opc
    elif not disponibilidad_profesional : 
        print("El profesional ya tiene reservado un turno en ese horario")
        opc = input("Ingrese '1' para cargar un turno en otro horario, '2' para volver al menu principal o '0' para cerrar sesion: ")
        if opc == "2" :
            menu()
            opc = input("Ingrese la opcion: ")
        return opc  
    return salir()
           
                     
# Funcion para mostrar los turnos del usuario
def mostrar_turnos_cliente(index, lista_clientes) :
    turnos_cliente = lista_clientes[index][1]
    if len(turnos_cliente) != 0 :
        print("Usted tiene los siguientes turnos reservados: ")
        for turno in turnos_cliente :
            print(turno[0] + ": " + turno[2] + " a las " + str(turno[3]))
            print("Profesional: " + turno[1])
    elif len(turnos_cliente) == 0 :
        print("Usted no tiene turnos reservados")
        opc = input("Ingrese '1' para reservar un turno, '2' para volver al menu principal o '0' para cerrar sesion: ")
        if opc == "2" :
            menu()
            opc = input("Ingrese la opcion: ")
        return opc
    return salir()
    

# Funcion para mostrar a los profesionales y sus turnos reservados o libres
def mostrar_turnos_profesionales(lista_profesionales) :
    print("Seleccione la especialidad a consultar: ")
    print("1- Barberia")
    print("2- Depilacion")
    print("3- Manicura")
    print("4- para volver al menu principal")
    opc = input("Ingrese la opcion deseada: ")
    while opc != "1" and opc != "2" and opc != "3" and opc != "4" :
        print("Error: debe ingresar el numero correspondiente a la especialidad")
        opc = input("Ingrese la opcion deseada: ")
    if opc == "4" :
        menu()
        opc = input("Ingrese la opcion: ")
        return opc
    elif opc == "1":
        for profesional in lista_profesionales :
            if profesional[1] == "barberia" :
                print(profesional[0])
                for horario in profesional[2] :
                    print(horario[0] + ": " + str(horario[1]) + "hs " + horario[2])
        opc = input("Ingrese '1' para consultar por otro profesional, '2' para volver al menu principal o '0' para cerrar sesion: ")
        if opc == "1" :
            opc = "3"
        if opc == "2" :
            menu()
            opc = input("Ingrese la opcion: ")
        return opc
    elif opc == "2":
        for profesional in lista_profesionales :
            if profesional[1] == "depilacion" :
                print(profesional[0])
                for horario in profesional[2] :
                    print(horario[0] + ": " + str(horario[1]) + "hs " + horario[2])
        opc = input("Ingrese '1' para consultar por otro profesional, '2' para volver al menu principal o '0' para cerrar sesion: ")
        if opc == "1" :
            opc = "3"
        if opc == "2" :
            menu()
            opc = input("Ingrese la opcion: ")
        return opc
    elif opc == "3":
        for profesional in lista_profesionales :
            if profesional[1] == "manicura" :
                print(profesional[0])
                for horario in profesional[2] :
                    print(horario[0] + ": " + str(horario[1]) + "hs " + horario[2])
        opc = input("Ingrese '1' para consultar por otro profesional, '2' para volver al menu principal o '0' para cerrar sesion: ")
        if opc == "1" :
            opc = "3"
        if opc == "2" :
            menu()
            opc = input("Ingrese la opcion: ")
        return opc
