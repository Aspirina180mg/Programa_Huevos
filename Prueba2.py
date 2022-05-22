#La empresa productora y comercializadora de huevos “All Eggs”, que está en constante expansión dentro del territorio 
#nacional, está automatizando sus procesos administrativos. Su misión es la de Producir, comercializar y distribuir 
#huevos de calidad. Para satisfacer la demanda dentro de estos procesos, se le ha solicitado a Usted como desarrollador
#en Python para dar solución, siguiendo las especificaciones que se explicitan a continuación:
#   1- All Eggs, distribuye los siguientes tipos de huevos: Gallina, Pato, Codorniz y Avestruz.
#   2- Control de Autentificación: El sistema debe contar con un control de autentificación. Es decir, al empezar el 
#      programa, deberá pedir Usuario y Contraseña. El usuario administrador inicial y contraseña los puede definir a su 
#      criterio.
#   3- Menú de opciones (post ingreso): Cuando el usuario accede al sistema, dispondrá de las siguientes opciones:
#       a. Asignación de precios de Huevos
#       b. Creación de despachos
#        c. Listar huevos
#        d. Listar despachos



#    4- Asignación de precios de los tipos de huevos: El usuario administrador del sistema, podrá asignar los precios 
#       de cada uno de los huevos. 
#        a. Reglas para la asignación de precio de los huevos:
#            i. El precio mínimo de la unidad para los huevos de Gallina es de $50
#            ii. El precio mínimo de la unidad para los huevos de Pato es de $150
#            iii. El precio mínimo de la unidad para los huevos de Codorniz es de $50
#            iv. El precio mínimo de la para los huevos de Avestruz es de $800
#    5- Creación de un despacho: Para generar un despacho, se deben considerar los siguientes datos:
#        a. Datos a Ingresar:
#            i. Correlativo del Despacho (ID)
#            ii. Rut del cliente
#            iii. Nombre o Razón Social
#            iv. Tipo de Huevo, en donde sólo se podrá ingresar uno de los tipos registrados, que en su defecto vendría
#                siendo: Gallina, Pato, Codorniz o Avestruz.
#            v. ¿Tiene Convenio? En dónde sólo se podrá ingresar Sí o no.
#            vi. Dirección (domicilio) a realizar el despacho.
#            vii. Fecha Comprometida (corresponde a la fecha en que se deben enviar los huevos)
#            viii. Cantidad de huevos a enviar.
#            ix. Terminado el registro, éste deberá quedar almacenado, indicando que el registro se realizó correctamente. 
#               Posterior a ello, debe volver al menú.
#        b. Datos a calcular:
#            i. Implícitamente, se deberá guardar el precio unitario del huevo, ya que el precio varía según la 
#               necesidad de la demanda.
#            ii. Después de realizar el ingreso de la cantidad de huevos, implícitamente se deberá calcular la cantidad
#                ingresada por precio unitario del momento del huevo.
#        c. Reglas a considerar:
#            i. Al registrar un despacho, los campos no deben estar vacíos.
#            ii. Los despachos NO SE DEBEN REPETIR (El id no debe estar duplicado) Considere que el id del despacho 
#               puede ser un número correlativo (acumulativo) en donde dicho ID será la KEY del diccionario.
#            iii. La cantidad mínima de huevos a enviar, deberán ser 50 y máximo 10000.
#            iv. En caso de tener convenio (Sí), el precio final del despacho tendrá un 10% de descuento.
#    6- Listar Huevos: el usuario autentificado, podrá ver todos los huevos disponibles, con sus respectivos precios 
#       unitarios.
#    7- Listar despachos: el usuario autentificado, podrá listar todos los despachos registrados en el sistema.
user_ = "admin"
pwd_= "1234"
print ("bienvenido ingrese sus datos para iniciar sesion")
print ("ingrese usuario: ")
user = input ()
print ("ingrese la contraseña: ")
pwd = input ()
if user == user_ and pwd == pwd_:
    print ("bienvenidos")
else :
    print ("usuario o contraseña invalido")
print ("\nMenú All Eggs\n\n--------------\n\n1)Asignación de precios de huevos\n\n2)Creación de despachos\n")
print ("\n3)Listar huevos\n\n4)Listar despachos\n")

menu = int (input ("» "))
print ("")
if menu == 1 :
    print ("Asignación de precios de Huevos")
elif menu == 2 :
    print("Creación de despachos")
elif menu == 3 :
    print ("Listar huevos")
elif menu == 4 :
    print ("Listar despachos")
else :
    print ("opción incorrecta")