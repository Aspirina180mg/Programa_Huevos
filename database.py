import mysql.connector

db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Mamago12', database = 'huevos')

print (db)

cursor = db.cursor()

#cursor.execute("insert into despachos (rut, nombre, tipo, convenio, direccion, cantidad, valor_unitario, valor_total) values ('18264014-k', 'Kimberly Moya Aliaga', 1, 1, 'Cerro Santa Rosa 3515 Block 4 Departamento 404, Iquique', 200, 50, 100000);")
#db.commit()
cursor.execute("select * from despachos")
resultado = cursor.fetchall()
for x in resultado:
    print (x)