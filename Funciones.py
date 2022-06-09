import os 
from database import *

def limpiar (): os.system ("cls" if os.name == "nt" else "clear")       #funcion para limpiar pantalla, funciona en windows o linux
def esperar (): input ("\nPulse Enter para continuar...")       #funcion de espera, requiere una entrada

def asignacion ():       #funcion para asignar valores distintos a los iniciales
    global valores
    navegacion = int(input ("elija el tipo de huevo al que le modificará el precio\n1) Gallina\n2) Pato\n3) Codorniz\n4) Avestruz\n>"))
    navegacion -= 1
    print ("el valor de los huevos de ", huevos [navegacion], " es de $", valores [navegacion])
    precio = int (input ("ingrese el nuevo valor\n>"))
    match navegacion:
        case 0 if precio < 50: print ("El precio del huevo de gallina debe ser mayor a 50")
        case 1 if precio < 150: print ("El precio del huevo de pato debe ser mayor a 150")
        case 2 if precio < 50: print ("El precio del huevo de codorniz debe ser mayor a 50")
        case 3 if precio < 800: print ("El precio del huevo de avestrúz debe ser mayor a 800")
        case _: valores[navegacion] = precio
    #todo
    #cursor.execute ('update productos set valor = %s where ID = 1', valores[navegacion])
    #db.commit()

def creacion ():     #funcion para crear despachos
    global ID       #se permite la modificacion de las variables ID, valores y despachos.
    global despachos
    ID += 1
    rut = input ("Ingrese RUT\n>")
    nombre = input ("Ingrese Nombre o Razon Social\n>")
    tipo_n = 5       #se apoya en el contador i para realizar el ciclo de tipo de huevos
    while tipo_n != 1 and tipo_n != 2 and tipo_n != 3 and tipo_n != 4:
        #limpiar ()
        tipo_n = int(input ("Seleccione un tipo de huevo:\n1) Gallina\n2) Pato\n3) Codorniz\n4) Avestruz\n>"))
        match tipo_n:
            case 1: tipo = "Gallina"
            case 2: tipo = "Pato"
            case 3: tipo = "Codorniz"
            case 4: tipo = "Avestruz"
            case _: print ("Ha ingresado una opción incorrecta, intente nuevamente")
    tipo_n -= 1
    convenio = 0
    i = input ('si el usuario posee convenio, ingrese "SI", de lo contrario, se asumirá que no existe convenio\n>')
    if i == "SI" or i == "si" or i == "Si" or i == "sI": convenio = 1       #se acepta independiente de la forma en que lo escriba
    direccion = input ("ingrese dirección\n>")
    cantidad =49
    while cantidad < 51 or cantidad > 9999:
        print ("la cantidad debe ser mayor a 50 y menor que 10.000")        #condiciones definidas previamente
        cantidad = int (input ("ingrese cantidad de huevos a enviar\n>"))
    limpiar ()
    valor = 1
    if convenio == 1: valor = 0.9       #de existir convenio, se fija el valor a un 90%
    if rut != "" and nombre != "" and direccion != "":
        lista = [rut, nombre, tipo, convenio, direccion, cantidad, valores[tipo_n] * valor, valor * valores [tipo_n] * cantidad]
        despachos [ID] = lista       #se almacenan los datos de la lista en el diccionario
        print ("el registro de despacho se ha realizado correctamente, con el ID ", ID)
    else:
        print("Ha ingresado datos vacios, este registro se anulara")
        ID -= 1

def listar ():       #funcion para listar los valores de los huevos
    print ("Huevos de Gallina:  $", valores [0], "\nHuevos de Pato:     $", valores [1],"\nHuevos de Codorniz: $", valores [2], "\nHuevos de Avestruz: $", valores [3])

def listar_despachos ():        #funcion para listar los despachos registrados
    print ("Los despachos registrados son:\n")
    for i in despachos.keys (): print ("ID ",i)     #navega a traves de los keys del diccionario
    print ()
    consulta = int (input ("ingrese el ID que desea consultar\n>"))
    limpiar ()
    if consulta in despachos:
        lista = despachos [consulta]     #se sacan los valores del diccionario, para poder trabajar con la lista
        print ("Rut:              ", lista [0],"\nNombre:           ", lista [1],"\nTipo de Huevo:    ", lista [2])
        if lista [3] == 1: print ("Posee convenio:    si")
        else: print ("Posee convenio:    no")
        print ("Direccion:        ", lista [4],"\ncantidad enviada: ", lista [5],"\nvalor unitario:  $", lista [6],"\nvalor total:     $", lista [7])
    else: print ("Ese no es un despacho valido")

def incorrecto ():       #funcion que se realizara al ingresar una opcion no valida en el menu
    if input ('para cerrar el programa ingrese la palabra "huevos"\n>') == "huevos": quit ()

cursor.execute("select * from productos")
query = cursor.fetchone()
val1 = query[2]
query = cursor.fetchone()
val2 = query[2]
query = cursor.fetchone()
val3 = query[2]
query = cursor.fetchone()
val4 = query[2]
valores = [val1, val2, val3, val4]        #gallina, pato, codorniz, avestruz
huevos = ["gallina","pato","codorniz","avestruz"]
ID = 101        #Identificador de Despacho
lista = ["18992359-7", "Misael Garcia", "Gallina", "si", "Avenida siempre viva 2785", 200, 45, 9000]
despachos = {100:lista}     #primer valor preasignado
lista = ["18899270-6", "Felipe Rojas", "Avestruz", "no", "Avenida siempre viva 2350", 100, 800, 80000]
despachos [101] = lista      #segundo valor preasignado