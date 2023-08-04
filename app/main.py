from flask import Flask, request, render_template
from config import *
app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')
@app.route('/form', methods=['GET', 'POST'])
def registrar_categoria():
    msg = ""
    if request.method == 'POST':
        nomCate = request.form['nomCate']
        conexion_MySQLdb = connectionBD()

        if conexion_MySQLdb:
            cursor = conexion_MySQLdb.cursor(dictionary=True)
            sql = "INSERT INTO categorias (nomCate) VALUES (%s)"
            valores = (nomCate,)
            cursor.execute(sql, valores)
            conexion_MySQLdb.commit()
            cursor.close()
            conexion_MySQLdb.close()
            msg = 'Registro con éxito'
            print(cursor.rowcount, "registro insertado")
            print("1 registro insertado, id", cursor.lastrowid)
        else:
            msg = 'Error en la conexión a la base de datos'

        return render_template('index.html', msg='Successfully')
    else:
        return render_template('index.html', msg='Método HTTP incorrecto')

# ... (resto de tu código)






if __name__== '__main__':
    app.run(debug=True,port=5000)