from Funciones import *
from database import *
entrada = None
i = 0       #variable para navegación en menú
while True:
    if entrada != 1:
        user = input ("==============\nLogin All Eggs\n==============\n\ningrese usuario: ")
        pwd = input ("ingrese la contraseña: ")       #se pide usuario y contraseña
    if user == query [0] and pwd == query [1]:
        if entrada != 1: 
            print ("\nAcceso concedido")
            entrada = 1
        esperar ()
        limpiar ()
        navegacion = input ("Menú All Eggs\n--------------\n1) Asignación de precios de huevos\n2) Creación de despachos\n3) Listar precios de huevos\n4) Listar despachos\notro)Salir\n>")
        limpiar ()
        match navegacion:
            case "1": asignacion ()
            case "2": creacion ()
            case "3": listar ()
            case "4": listar_despachos ()
            case   _: incorrecto ()
        continue
    else:
        print ("\nusuario o contraseña invalido\nintento Numerno", i + 1 , "de 3")
        i += 1        #aumenta contador
        if i > 2:
            #limpiar ()
            print ("Ha fallado 3 veces el inicio de sesion, se cerrara el programa")
            quit()
        esperar ()