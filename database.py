import mysql.connector

#Conexión con Base de datos
db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Mamago12', database = 'huevos')
#navegación y selección de datos de login
cursor = db.cursor()
cursor.execute("select * from login")
query = cursor.fetchone()