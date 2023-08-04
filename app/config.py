import mysql.connector

def connectionBD():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="proyecto_personalizacion_articulos"
        )
        print("Conexion exitosa")
        return mydb
    except mysql.connector.Error as err:
        print("Error en la conexion a BD:", err)
        return None
