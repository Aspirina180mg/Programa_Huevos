'''
Creado por
Misael Garcia   18.992.359-7
Felipe Rojas    18.899.270-6
Estudiantes de Ingeniería en Informática
Ramo de Estructuras de datos y algoritmos
Profesor David Villegas
generación 2022 horario vespertino
'''

import os

def limpiar ():      #funcion para limpiar pantalla, funciona en windows o linux
    os.system ('cls' if os.name == 'nt' else 'clear') 

def esperar ():      #funcion de espera, requiere una entrada
    input ("\nPulse Enter para continuar...")
    
def menu ():        #funcion para la navegacion del menu, llamara las funciones correspondientes
    limpiar ()
    print ("\nMenú All Eggs\n--------------\n1) Asignación de precios de huevos")
    print ("2) Creación de despachos\n3) Listar precios de huevos\n4) Listar despachos")
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
    global valores
    limpiar ()
    navegacion = input ("elija el tipo de huevo al que le modificará el precio\n1) Gallina\n2) Pato\n3) Codorniz\n4) Avestruz\n>")
    if navegacion == "1":
        print ("el valor de los huevos de gallina es de $", valores [0])
        precio = int (input ("ingrese el nuevo valor\n>"))
        if precio < 50:
            print ("El precio del huevo de gallina debe ser mayor a 50")
        else:
            valores [0] = precio
    elif navegacion == "2":
        print ("el valor de los huevos de pato es de $", valores [1])
        precio = int (input ("ingrese el nuevo valor\n>"))
        if precio < 150:
            print ("El precio del huevo de pato debe ser mayor a 150")
        else:
            valores [1] = precio
    elif navegacion == "3":
        print ("el valor de los huevos de codorniz es de $", valores [2])
        precio = int (input ("ingrese el nuevo valor\n>"))
        if precio < 50:
            print ("El precio del huevo de codorniz debe ser mayor a 50")
        else:
            valores [2] = precio
    elif navegacion == "4":
        print ("el valor de los huevos de avestruz es de $", valores [3])
        precio = int (input ("ingrese el nuevo valor\n>"))
        if precio < 800:
            print ("El precio del huevo de avestrúz debe ser mayor a 800")
        else:
            valores [3] = precio
    else:
        print ("Esa no es una opcion valida")
    esperar ()
    menu ()

def creacion ():     #funcion para crear despachos

    def construir_fecha (d, m, a):
        d = str(d)
        m = str(m)
        a = str(a)
        fecha = d+"/"+m+"/"+a
        return fecha

    global ID       #se permite la modificacion de las variables ID, valores y despachos.
    global valores
    global despachos
    limpiar ()
    ID += 1
    rut = ""        #todos los valores de la lista se inician como "" para el control de ingreso vacio
    while rut == "":
        rut = input ("Ingrese RUT\n>")
    limpiar ()
    nombre=""
    while nombre == "":
        nombre = input ("Ingrese Nombre o Razon Social\n>")
    limpiar ()
    i = 5       #se apoya en el contador i para realizar el ciclo de tipo de huevos
    while i !=  "1" and i != "2" and i != "3" and i != "4":
        limpiar ()
        i = input ("Seleccione un tipo de huevo:\n1) Gallina\n2) Pato\n3) Codorniz\n4) Avestruz\n>")
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
        cantidad = int (input ("ingrese cantidad de huevos a enviar\n>"))
        if cantidad < 50 or cantidad > 10000:
            print ("el monto debe ser mayor a 50 y menor que 10.000")        #condiciones definidas previamente
        else:
            break
    limpiar ()
    fecha = ""
    while fecha == "":
        año = int (input ("ingrese el año con 4 dígitos, debe ser mayor a 2021"))
        limpiar ()
        mes = int(input ("ingrese mes como número, debe estar entre 1 y 12"))
        limpiar ()
        dia = int(input ("ingrese día como número, debe ser un dia válido para el mes elegido"))
        if año > 2021:
            if mes > 0 and mes < 13:
                match mes:
                    case 1:
                        if dia > 0 and dia < 32: fecha = construir_fecha (dia, mes, año)
                    case 2:
                        if dia > 0 and dia < 29: fecha = construir_fecha (dia, mes, año)
                    case 3:
                        if dia > 0 and dia < 32: fecha = construir_fecha (dia, mes, año)
                    case 4:
                        if dia > 0 and dia < 31: fecha = construir_fecha (dia, mes, año)
                    case 5:
                        if dia > 0 and dia < 32: fecha = construir_fecha (dia, mes, año)
                    case 6:
                        if dia > 0 and dia < 31: fecha = construir_fecha (dia, mes, año)
                    case 7:
                        if dia > 0 and dia < 32: fecha = construir_fecha (dia, mes, año)
                    case 8:
                        if dia > 0 and dia < 32: fecha = construir_fecha (dia, mes, año)
                    case 9:
                        if dia > 0 and dia < 31: fecha = construir_fecha (dia, mes, año)
                    case 10:
                        if dia > 0 and dia < 32: fecha = construir_fecha (dia, mes, año)
                    case 11:
                        if dia > 0 and dia < 31: fecha = construir_fecha (dia, mes, año)
                    case 12:
                        if dia > 0 and dia < 32: fecha = construir_fecha (dia, mes, año)
    limpiar ()
    valor = 1
    if convenio == 1:       #de existir convenio, se fija el valor a un 90%
        valor = 0.9
    valor = valor * valores [tipo_n] * cantidad      #se calcula el valor total de la carga
    precio_unitario = valor / cantidad        #se almacena tomando en cuenta el convenio o solo el valor del huevo?
    lista = [rut, nombre, tipo, convenio, direccion, cantidad, fecha, precio_unitario, valor]
    despachos [ID] = lista       #se almacenan los datos de la lista en el diccionario
    print ("el registro de despacho se ha realizado correctamente, con el ID ", ID)
    esperar ()
    menu ()

def listar ():       #funcion para listar los valores de los huevos
    limpiar ()      #la linea 104 esta dividida por el "\"
    print ("Huevos de Gallina:  $", valores [0], "\nHuevos de Pato:     $", valores [1],\
    "\nHuevos de Codorniz: $", valores [2], "\nHuevos de Avestruz: $", valores [3])
    esperar ()
    menu ()

def listar_despachos ():        #funcion para listar los despachos registrados
    limpiar ()
    print ("\nMenú listar despachos\n--------------\n1) Buscar por Fecha\n2) Buscar por Rut\n3) Buscar por Nombre o Razón Social\n4) Listar todo")
    navegacion = input ("otro)Volver\n>")
    if navegacion == "1" :      #Buscar por Fecha
        año = int (input ("ingrese el año a consultar\n"))
        limpiar ()
        mes = int(input ("ingrese mes a consultar\n"))
        limpiar ()
        dia = int(input ("ingrese día a consultar\n"))
        busqueda = str(dia) + "/" + str(mes) + "/" + str(año)
        limpiar()
        contador = 0
        for i in despachos.keys ():      #navega a traves de los keys del diccionario
            lista = despachos [i]     #se sacan los valores del diccionario, para poder trabajar con la lista
            if lista[6] == busqueda:
                contador += 1
                print ("Rut:               ", lista [0])
                print ("Nombre:            ", lista [1])
                print ("Tipo de Huevo:     ", lista [2])
                if lista [3] == 1:
                    print ("Posee convenio:     si")
                else:
                    print ("Posee convenio:     no")
                print ("Direccion:         ", lista [4])
                print ("cantidad enviada:  ", lista [5])
                print ("fecha comprometida:", lista [6])
                print ("valor unitario:   $", lista [7])
                print ("valor total:      $", lista [8])           
        if contador == 0:
            print("No se ha encontrado")
    elif navegacion == "2" :        #Buscar por Rut
        busqueda = str (input ("ingrese el rut a consultar\n"))
        limpiar ()
        contador = 0
        for i in despachos.keys ():      #navega a traves de los keys del diccionario
            lista = despachos [i]     #se sacan los valores del diccionario, para poder trabajar con la lista
            if lista[0] == busqueda:
                contador += 1
                print ("Rut:               ", lista [0])
                print ("Nombre:            ", lista [1])
                print ("Tipo de Huevo:     ", lista [2])
                if lista [3] == 1:
                    print ("Posee convenio:     si")
                else:
                    print ("Posee convenio:     no")
                print ("Direccion:         ", lista [4])
                print ("cantidad enviada:  ", lista [5])
                print ("fecha comprometida:", lista [6])
                print ("valor unitario:   $", lista [7])
                print ("valor total:      $", lista [8])           
        if contador == 0:
            print("No se ha encontrado")
    elif navegacion == "3" :        #Buscar por Nombre o Razón Social
        busqueda = str (input ("ingrese palabra a buscar en nombre o razón social (recuerde que se diferencia de mayúsculas y minúsculas)\n"))
        limpiar ()
        contador = 0
        for i in despachos.keys ():      #navega a traves de los keys del diccionario
            lista = despachos [i]     #se sacan los valores del diccionario, para poder trabajar con la lista
            if busqueda in lista[1]:
                contador += 1
                print ("Rut:               ", lista [0])
                print ("Nombre:            ", lista [1])
                print ("Tipo de Huevo:     ", lista [2])
                if lista [3] == 1:
                    print ("Posee convenio:     si")
                else:
                    print ("Posee convenio:     no")
                print ("Direccion:         ", lista [4])
                print ("cantidad enviada:  ", lista [5])
                print ("fecha comprometida:", lista [6])
                print ("valor unitario:   $", lista [7])
                print ("valor total:      $", lista [8])           
        if contador == 0:
            print("No se ha encontrado")
    elif navegacion == "4" :        #Listar Todo
        print ("Los despachos registrados son:\n")
        for i in despachos.keys ():      #navega a traves de los keys del diccionario
            consulta = int (i)
            lista = despachos [consulta]     #se sacan los valores del diccionario, para poder trabajar con la lista
            if lista [3] == 1:
                convenio = "Posee convenio: si"
            else:
                convenio = "Posee convenio: no"
            print ("ID: ",i ,", Rut: ", lista [0], ", Nombre: ", lista [1], ", Tipo de Huevo: " , lista [2], ",")
            print (convenio, ", Direccion: ", lista [4], ", Cantidad enviada: ", lista [5], ",")
            print ("Fecha comprometida: ", lista [6], ", Valor unitario: $", lista [7], ", Valor total: $", lista [8], "\n")
    else :
        print ("volviendo al Menú...")
    esperar ()
    menu ()

def incorrecto ():       #funcion que se realizara al ingresar una opcion no valida en el menu
    limpiar ()
    print ('para cerrar el programa ingrese la palabra "huevos"')
    salida = input (">")     #seguridad para evitar salir por error
    if salida == "huevos":
        quit ()
    else:
        menu ()

valores = [50, 150, 50, 800]        #gallina, pato, codorniz, avestruz
user_ = "admin"     #usuario esperado
pwd_ = "1234"       #contraseña esperada
i = 0       #variable para navegación en menú
ID = 101        #Identificador de Despacho
lista = ["18992359-7", "Misael Garcia", "Gallina", "si", "Avenida siempre viva 2785", 200, "22/1/2022", 45, 9000]
despachos = {100:lista}     #primer valor preasignado
lista = ["18899270-6", "Felipe Rojas", "Avestruz", "no", "Avenida siempre viva 2350", 100, "29/1/2022", 800, 80000]
despachos [101] = lista      #segundo valor preasignado
print ("Bienvenido, ingrese sus datos para iniciar sesion\n")
while 0 == 0:
    user = input ("ingrese usuario: ")
    pwd = input ("ingrese la contraseña: ")       #se pide usuario y contraseña
    if user == user_ and pwd == pwd_:
        menu ()
    else :
        print ("\nusuario o contraseña invalido\nintento Numerno", i + 1 , "de 3")
        i += 1        #aumenta contador
        esperar ()
        limpiar ()
        if i == 3 :
            print ("Ha fallado 3 veces el inicio de sesion, se cerrara el programa")
            esperar ()
            break