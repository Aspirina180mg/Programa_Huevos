'''
La empresa productora y comercializadora de huevos “All Eggs”, que está en constante expansión dentro del territorio nacional, está automatizando sus procesos administrativos. Su misión es la de Producir, comercializar y distribuir huevos de calidad. Para satisfacer la demanda dentro de estos procesos, se le ha solicitado a Usted como desarrollador en Python para dar solución, siguiendo las especificaciones que se explicitan a continuación:
1-	All Eggs, distribuye los siguientes tipos de huevos: Gallina, Pato, Codorniz y Avestruz.
2-	Control de Autentificación: El sistema debe contar con un control de autentificación. Es decir, al empezar el programa, deberá pedir Usuario y Contraseña. El usuario administrador inicial y contraseña los puede definir a su criterio.
3-	Menú de opciones (post ingreso): Cuando el usuario accede al sistema, dispondrá de las siguientes opciones:
    a.	Asignación de precios de Huevos
    b.	Creación de despachos
    c.	Listar huevos
    d.	Listar despachos
4-	Asignación de precios de los tipos de huevos: El usuario administrador del sistema, podrá asignar los precios de cada uno de los huevos. 
    a.	Reglas para la asignación de precio de los huevos:
        i.	El precio mínimo de la unidad para los huevos de Gallina es de $50
        ii.	El precio mínimo de la unidad para los huevos de Pato es de $150
        iii.	El precio mínimo de la unidad para los huevos de Codorniz es de $50
        iv.	El precio mínimo de la para los huevos de Avestruz es de $800
5-	Creación de un despacho: Para generar un despacho, se deben considerar los siguientes datos:
    a.	Datos a Ingresar:
        i.	Correlativo del Despacho (ID)
        ii.	Rut del cliente
        iii.	Nombre o Razón Social
        iv.	Tipo de Huevo, en donde sólo se podrá ingresar uno de los tipos registrados, que en su defecto vendría siendo: Gallina, Pato, Codorniz o Avestruz.
        v.	¿Tiene Convenio? En dónde sólo se podrá ingresar Sí o no.
        vi.	Dirección (domicilio) a realizar el despacho.
        vii.	Fecha Comprometida (corresponde a la fecha en que se deben enviar los huevos)
        viii.	Cantidad de huevos a enviar.
        ix.	Terminado el registro, éste deberá quedar almacenado, indicando que el registro se realizó correctamente. Posterior a ello, debe volver al menú.
    b.	Datos a calcular:
        i.	Implícitamente, se deberá guardar el precio unitario del huevo, ya que el precio varía según la necesidad de la demanda.
        ii.	Después de realizar el ingreso de la cantidad de huevos, implícitamente se deberá calcular la cantidad ingresada por precio unitario del momento del huevo.
    c.	Reglas a considerar:
        i.	Al registrar un despacho, los campos no deben estar vacíos.
        ii.	Los despachos NO SE DEBEN REPETIR (El id no debe estar duplicado) Considere que el id del despacho puede ser un número correlativo (acumulativo) en donde dicho ID será la KEY del diccionario.
        iii.	La cantidad mínima de huevos a enviar, deberán ser 50 y máximo 10000.
        iv.	En caso de tener convenio (Sí), el precio final del despacho tendrá un 10% de descuento.
6-	Listar Huevos: el usuario autentificado, podrá ver todos los huevos disponibles, con sus respectivos precios unitarios.
7-	Listar despachos: el usuario autentificado, podrá listar todos los despachos registrados en el sistema, así como también realizar búsqueda por fechas comprometidas.

Requerimientos Adicionales
1.	Utilizando lenguaje de programación Python, debe crear los menús necesarios para dar solución a la problemática.
2.	Debe ser validado el ingreso de datos para no interrumpir el flujo del programa.
3.	Determinar funciones necesarias para cada ítem de cada menú,  considerar al implementar seguir secuencia lógica necesaria para esto.
4.	Control de autentificación inicial.
5.	Los menús a crear son:
    a.	Asignación de precios de Huevos
    b.	Creación de despachos
    c.	Listar huevos
    d.	Listar despachos con las siguientes sub-opciones:
        i.	Buscar por Fecha comprometida
        ii.	Buscar por Rut
        iii.	Listar todo
        iv.	Buscar despachos por razón social: Se deberán realizar búsquedas por la proximidad de una razón social existente. Por ejemplo:
            1.	Si tenemos registrado los despachos con las razones sociales “Comercializadora X” y “Comercio AyB Ltda.” Y yo como usuario busco por “comer”, se deberá listar los despachos de ambas razones sociales porque la palabra “comer” existe en ambas razones sociales.
6.	Creación correcta de variables.
7.	Modificar los huevos según reglas de negocios establecidas
    a.	Considerar reglas de negocios apoyándose en funciones definidas que Python provee.
8.	Ingreso correcto del despacho a realizar.
    a.	Considerar reglas de negocios apoyándose en funciones definidas que Python provee.
9.	Utilizar listas que permitan modificar la información de los huevos.
10.	Utilizar un Diccionario para el registro de los despachos.
11.	Limpieza y orden en el entregable final.
'''

'''
Misael Garcia   18.992.359-7
Felipe Rojas    18.899.270-6
Estudiantes de Ingenieria en Informatica, generacion 2022 horario vespertino
Ramo de estructuras de datos y algoritmos, profesor David Villegas
'''
import os
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

valores = [50, 150, 50, 800]        #gallina, pato, codorniz, avestruz
huevos = ["gallina","pato","codorniz","avestruz"]
i = 0       #variable para navegación en menú
ID = 101        #Identificador de Despacho
lista = ["18992359-7", "Misael Garcia", "Gallina", "si", "Avenida siempre viva 2785", 200, 45, 9000]
despachos = {100:lista}     #primer valor preasignado
lista = ["18899270-6", "Felipe Rojas", "Avestruz", "no", "Avenida siempre viva 2350", 100, 800, 80000]
despachos [101] = lista      #segundo valor preasignado
entrada = None
while 0 == 0:
    if entrada != 1:
        user = input ("Login\n\nSi falla 3 veces, este programa se cerrara\n\ningrese usuario: ")
        pwd = input ("ingrese la contraseña: ")       #se pide usuario y contraseña
    match user:
        case "admin" if pwd == "1234":
            if entrada != 1: 
                print ("\nAcceso concedido")
                entrada = 1
            esperar()
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
        case _ if pwd != "1234":
            print ("\nusuario o contraseña invalido\nintento Numerno", i + 1 , "de 3")
            i += 1        #aumenta contador
            if i > 2:
                limpiar ()
                print ("Ha fallado 3 veces el inicio de sesion, se cerrara el programa")
                quit()
            esperar ()