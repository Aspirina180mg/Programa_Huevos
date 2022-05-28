'''
La empresa productora y comercializadora de huevos “All Eggs”, que está en constante expansión dentro del territorio nacional, está automatizando sus procesos administrativos. Su misión es la de Producir, comercializar y distribuir huevos de calidad. Para satisfacer la demanda dentro de estos procesos, se le ha solicitado a Usted como desarrollador en Python para dar solución, siguiendo las especificaciones que se explicitan a continuación:
    1- All Eggs, distribuye los siguientes tipos de huevos: Gallina, Pato, Codorniz y Avestruz.
    2- Control de Autentificación: El sistema debe contar con un control de autentificación. Es decir, al empezar el programa, deberá pedir Usuario y Contraseña. El usuario administrador inicial y contraseña los puede definir a su criterio.
    3- Menú de opciones (post ingreso): Cuando el usuario accede al sistema, dispondrá de las siguientes opciones:
        a. Asignación de precios de Huevos
        b. Creación de despachos
        c. Listar huevos
        d. Listar despachos
'''
#   4- Asignación de precios de los tipos de huevos: El usuario administrador del sistema, podrá asignar los precios de cada uno de los huevos. 
#       a. Reglas para la asignación de precio de los huevos:
#           i. El precio mínimo de la unidad para los huevos de Gallina es de $50
#           ii. El precio mínimo de la unidad para los huevos de Pato es de $150
#           iii. El precio mínimo de la unidad para los huevos de Codorniz es de $50
#           iv. El precio mínimo de la para los huevos de Avestruz es de $800

#   5- Creación de un despacho: Para generar un despacho, se deben considerar los siguientes datos:
#       a. Datos a Ingresar:
#           i. Correlativo del Despacho (ID)
#           ii. Rut del cliente
#           iii. Nombre o Razón Social
#           iv. Tipo de Huevo, en donde sólo se podrá ingresar uno de los tipos registrados, que en su defecto vendría siendo: Gallina, Pato, Codorniz o Avestruz.
#           v. ¿Tiene Convenio? En dónde sólo se podrá ingresar Sí o no.
#           vi. Dirección (domicilio) a realizar el despacho.
#           viii. Cantidad de huevos a enviar.
#           ix. Terminado el registro, éste deberá quedar almacenado, indicando que el registro se realizó correctamente. Posterior a ello, debe volver al menú.

#       b. Datos a calcular:
#           i. Implícitamente, se deberá guardar el precio unitario del huevo, ya que el precio varía según la necesidad de la demanda.
#           ii. Después de realizar el ingreso de la cantidad de huevos, implícitamente se deberá calcular la cantidad ingresada por precio unitario del momento del huevo.

#       c. Reglas a considerar:
#           i. Al registrar un despacho, los campos no deben estar vacíos.
#           ii. Los despachos NO SE DEBEN REPETIR (El id no debe estar duplicado) Considere que el id del despacho puede ser un número correlativo (acumulativo) en donde dicho ID será la KEY del diccionario.
#           iii. La cantidad mínima de huevos a enviar, deberán ser 50 y máximo 10000.
#           iv. En caso de tener convenio (Sí), el precio final del despacho tendrá un 10% de descuento.
#   7- Listar despachos: el usuario autentificado, podrá listar todos los despachos registrados en el sistema.

import os

def limpiar ():      #funcion para limpiar pantalla, funciona en windows o linux
    os.system('cls' if os.name=='nt' else 'clear') 

def esperar():      #funcion de espera, requiere una entrada, independiente del tipo
    input ("\nPulse Enter para continuar...")

def menu ():
    limpiar ()
    navegacion = int (input ("\nMenú All Eggs\n--------------\n1)Asignación de precios de huevos\n2)Creación de despachos\n3)Listar huevos\n4)Listar despachos\n> "))
    if navegacion == 1 :
        asignacion ()
    elif navegacion == 2 :
        identificador = creacion (identificador)
    elif navegacion == 3 :
        listar ()
    elif navegacion == 4 :
        despachos ()
    else :
        incorrecto ()

def asignacion ():       #funcion relacionada con el punto 4 del ejercicio
    limpiar ()
    
    print ("Asignacion de precios")
    
    esperar()
    menu ()

def creacion (A):     #funcion relacionada con el punto 5 del jercicio
    limpiar ()
    A += 1
    rut = int (input ("Ingrese RUT asociado al despacho\n(ingrese con digito verificador, sin guion)\n>"))
    nombre = input ("Ingrese Nombre o Razon Social\n>")
    i = 5
    while i !=  1 and i != 2 and i != 3 and i != 4:
        i = input("Seleccione un tipo de huevo:\n1)Gallina\n2)Pato\n3)Codorniz\n4)Avestruz\n>")
        if i == 1:
            tipo = "Gallina"
            tipo_n = 0
        elif i == 2:
            tipo = "Pato"
            tipo_n = 1
        elif i == 3:
            tipo = "Codorniz"
            tipo_n = 2
        elif i == 4:
            tipo = "Avestruz"
            tipo_n = 3
        else:
            print ("Ha ingresado una opción incorrecta, intente nuevamente")
            limpiar()
    i = input ('si el usuariop posee convenio, ingrese "SI", de lo contrario, se asumirá que no existe convenio\n>')
    if i == "SI" or i == "si" or i == "Si" or i == "sI":
        convenio = 1
    else:
        convenio = 0
    direccion = input ("ingrese dirección\n>")
    while 0 == 0:
        cantidad = int(input("ingrese cantidad de huevos a enviar"))
        if cantidad < 50 or cantidad > 10000:
            print("el monto debe ser mayor a 50 y menor que 10.000")
        else:
            break
    valor = 1
    if convenio == 1:
        valor = 0.9
    valor = valor * valores[tipo_n]
    precio_unitario = valor/cantidad        #se almacena tomando en cuenta el convenio o solo el valor del huevo?
    if A !="" and rut !="" and nombre !="" and tipo !="" and convenio !="" and direccion !="" and cantidad !="" and precio_unitario !="":
        lista = [A, rut, nombre, tipo, convenio, direccion, cantidad, precio_unitario, ]    
        print ("el registro de despacho se ha realizado correctamente, con el ID ", A)
    else:
        print ("ha ingresado un dato vacío, se anulará la creación de este despacho")
        A = A - 1
    return A
    esperar()
    menu ()

#Después de realizar el ingreso de la cantidad de huevos, implícitamente se deberá calcular la cantidad ingresada por precio unitario del momento del huevo???

def listar ():       #funcion para listar los valores de los huevos
    limpiar ()
    print ("Huevos de Gallina:  $", valores [0], "\nHuevos de Pato:     $",valores [1], "\nHuevos de Codorniz: $", valores [2], "\nHuevos de Avestruz: $", valores[3])
    esperar()
    menu ()

def despachos ():        #funcion relacionada con el punto 7 del ejercicio
    limpiar ()
#    ID=input("Por favor ingrese ID que desea consultar en detalle")
#    print(Despachos(ID))
    print ("Listar despachos")
    esperar()
    menu ()

def incorrecto ():       #funcion que se realizara al ingresar una opcion no valida en el menu
    limpiar ()
    print ("opción incorrecta")
    esperar()
    menu ()

valores = [50, 150, 50, 800] #gallina, pato, codorniz, avestruz
user_ = "admin"     #usuario esperado
pwd_ = "1234"       #contraseña esperada
i = 0     #variable para navegación en menú
identificador = 100000       #Identificador de Despacho
'''
print ("Bienvenido, ingrese sus datos para iniciar sesion\n")
while 0 == 0:
    user = input ("ingrese usuario: "); pwd = input ("ingrese la contraseña: ")       #se pide usuario y contraseña
    if user == user_ and pwd == pwd_:
        menu ()
    else :
        print ("\nusuario o contraseña invalido\nintento Numerno", i+1 , "de 3"); i += 1        #aumenta contador
        esperar(); limpiar ()
        if i == 3 :
            print ("Ha fallado 3 veces el inicio de sesion, se cerrara el programa"); esperar(); break
'''
creacion(identificador)