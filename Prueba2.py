'''
Creado por 
Misael Garcia   18.992.359-7
Felipe Rojas    
Estudiantes de Ingenieria en Informatica 
Ramo de Estructuras de datos y algoritmos
generacion 2022 horario vespertino
'''
import os

def limpiar ():      #funcion para limpiar pantalla, funciona en windows o linux
    os.system('cls' if os.name=='nt' else 'clear') 

def esperar():      #funcion de espera, requiere una entrada
    input ("\nPulse Enter para continuar...")

def menu ():        #funcion para la navegacion del menu, llamara las funciones correspondientes
    limpiar ()
    print ("\nMenú All Eggs\n--------------\n1) Asignación de precios de huevos")
    print ("2) Creación de despachos\n3) Listar huevos\n4) Listar despachos")
    navegacion = input ("otro)Salir\n>")
    if navegacion == "1" :
        asignacion ()
    elif navegacion == "2" :
        creacion ()
    elif navegacion == "3" :
        listar ()
    elif navegacion == "4" :
        listar_despachos ()
    else :
        incorrecto ()

def asignacion ():       #funcion para asignar valores distintos a los iniciales
    limpiar ()
    
    print ("Asignacion de precios")
    
    esperar()
    menu ()

def creacion ():     #funcion para crear despachos
    global ID       #se permite la modificacion de las variables ID, valores y despachos.
    global valores
    global despachos
    limpiar ()
    ID += 1
    rut = ""        #todos los valores de la lista se inician como "" para el control de ingreso vacio
    while rut == "":
        rut = input ("Ingrese RUT\n>")
    limpiar()
    nombre=""
    while nombre == "":
        nombre = input ("Ingrese Nombre o Razon Social\n>")
    limpiar()
    i = 5       #se apoya en el contador i para realizar el ciclo de tipo de huevos
    while i !=  "1" and i != "2" and i != "3" and i != "4":
        limpiar()
        i = input("Seleccione un tipo de huevo:\n1) Gallina\n2) Pato\n3) Codorniz\n4) Avestruz\n>")
        if i == "1":
            tipo = "Gallina"
            tipo_n = 0
        elif i == "2":
            tipo = "Pato"
            tipo_n = 1
        elif i == "3":
            tipo = "Codorniz"
            tipo_n = 2
        elif i == "4":
            tipo = "Avestruz"
            tipo_n = 3
        else:
            print ("Ha ingresado una opción incorrecta, intente nuevamente")
    limpiar ()
    i = input ('si el usuario posee convenio, ingrese "SI", de lo contrario, se asumirá que no existe convenio\n>')
    if i == "SI" or i == "si" or i == "Si" or i == "sI":        #se acepta independiente de la forma en que lo escriba
        convenio = 1
    else:
        convenio = 0
    limpiar ()
    direccion = ""
    while direccion == "":
        direccion = input ("ingrese dirección\n>")
    limpiar ()
    while 0 == 0:
        cantidad = int(input("ingrese cantidad de huevos a enviar\n>"))
        if cantidad < 50 or cantidad > 10000:
            print("el monto debe ser mayor a 50 y menor que 10.000")        #condiciones definidas previamente
        else:
            break
    limpiar ()
    valor = 1
    if convenio == 1:       #de existir convenio, se fija el valor a un 90%
        valor = 0.9
    valor = valor * valores[tipo_n] * cantidad      #se calcula el valor total de la carga
    precio_unitario = valor/cantidad        #se almacena tomando en cuenta el convenio o solo el valor del huevo?
    lista = [rut, nombre, tipo, convenio, direccion, cantidad, precio_unitario]
    despachos[ID] = lista       #se almacenan los datos de la lista en el diccionario
    print ("el registro de despacho se ha realizado correctamente, con el ID ", ID)
    esperar()
    menu ()

def listar ():       #funcion para listar los valores de los huevos
    limpiar ()      #la linea 104 esta dividida por el "\"
    print ("Huevos de Gallina:  $", valores [0], "\nHuevos de Pato:     $", valores [1],\
    "\nHuevos de Codorniz: $", valores [2], "\nHuevos de Avestruz: $", valores[3])
    esperar()
    menu ()

def listar_despachos ():        #funcion para listar los despachos registrados
    limpiar ()
    print("Los despachos registrados son:\n")
    for i in despachos.keys():      #navega a traves de los keys del diccionario
        print(i)
    print()
    consulta = int(input("ingrese el numero de despacho que desea consultar\n>"))
    limpiar()
    if consulta in despachos:
        lista = despachos[consulta]     #se sacan los valores del diccionario, para poder trabajar con la lista
        print ("Rut:              ", lista[0])
        print ("Nombre:           ", lista[1])
        print ("Tipo de Huevo:    ", lista[2])
        print ("Posee convenio:   ", lista[3])
        print ("Direccion:        ", lista[4])
        print ("cantidad enviada: ", lista[5])
        print ("valor unitario:   ", lista[6])
    else:
        limpiar()
        print ("Ese no es un despacho valido")
    esperar()
    menu ()

def incorrecto ():       #funcion que se realizara al ingresar una opcion no valida en el menu
    global user
    limpiar ()
    print ('para cerrar el programa ingrese la palabra "huevos"')
    salida = input(">")     #seguridad para evitar salir por error
    if salida == "huevos":
        quit()
    else:
        menu ()

valores = [50, 150, 50, 800]        #gallina, pato, codorniz, avestruz
user_ = "admin"     #usuario esperado
pwd_ = "1234"       #contraseña esperada
i = 0       #variable para navegación en menú
ID = 101        #Identificador de Despacho
lista = ["18992359-7", "Misael Garcia", "Gallina", "convenio", "avenida siempre viva 2785", 200, 45]
despachos = {100:lista}     #primer valor preasignado
lista = ["18264014-k", "Felipe Rojas", "Avestruz", "sin convenio", "Avenida siempre viva 2350", 100, 800]
despachos[101] = lista      #segundo valor preasignado

print ("Bienvenido, ingrese sus datos para iniciar sesion\n")
while 0 == 0:
    user = input ("ingrese usuario: ")
    pwd = input ("ingrese la contraseña: ")       #se pide usuario y contraseña
    if user == user_ and pwd == pwd_:
        menu ()
    else :
        print ("\nusuario o contraseña invalido\nintento Numerno", i+1 , "de 3")
        i += 1        #aumenta contador
        esperar()
        limpiar ()
        if i == 3 :
            print ("Ha fallado 3 veces el inicio de sesion, se cerrara el programa")
            esperar()
            break