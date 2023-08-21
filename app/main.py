from flask import Flask, request, render_template
from config import *

app=Flask(__name__)


@app.route('/')
def inicioww():
    return render_template('index.html')
@app.route('/form', methods=['GET', 'POST'])
def registrar_categoria():
    msg = ""
    if request.method == 'POST':
        nomCate = request.form['nomCate']; 
        conexion_MySQLdb = connectionBD()

        if conexion_MySQLdb:
            cursor = conexion_MySQLdb.cursor(dictionary = True)
            sql = "INSERT INTO categorias (nomCate) VALUES (%s)"
            valores = (nomCate,)
            cursor.execute(sql, valores)
            conexion_MySQLdb.commit()
            cursor.close()
            conexion_MySQLdb.close()
            msg = 'Registro con éxito'
            print(cursor.rowcount, "Registro insertado")
            print("1 registro insertado, id", cursor.lastrowid)
        else:
            msg = 'Error en la conexión a la base de datos'

        return render_template('index.html', msg='Successfully')
    else:
        return render_template('index.html', msg='Método HTTP incorrecto')


#Formulario Cristian
@app.route('/formulario_cliente')
def inicio_clie():
    return render_template('formulario_cliente.html')
@app.route('/registrarclie', methods=['GET', 'POST'])




def registrar_cliente():
    msg = ""
    if request.method == 'POST':
        nomClie = request.form['nomClie']
        apellidoClie = request.form['apellidoClie']
        email = request.form['email']
        telClie = request.form['telClie']
        usuario = request.form['usuario']
        passw = request.form['password']  # Corregido: 'password' en lugar de 'passw'


        conexion_MySQLdb = connectionBD()

        if conexion_MySQLdb:
            cursor = conexion_MySQLdb.cursor(dictionary=True)
            sql = "INSERT INTO cliente (nomClie, apellidoCli, email, telClie, usuario, passw) VALUES (%s, %s, %s, %s, %s, %s)"  # Corregido: 'password' en lugar de 'pass'
            valores = (nomClie, apellidoClie, email, telClie, usuario, passw)
            cursor.execute(sql, valores)
            conexion_MySQLdb.commit()
            cursor.close()
            conexion_MySQLdb.close()
            msg = 'Registro con éxito'
            print(cursor.rowcount, "registro insertado")
            print("1 registro insertado, id", cursor.lastrowid)
        else:
            msg = 'Error en la conexión a la base de datos'

        return render_template('formulario_cliente.html', msg='Successfully')
    else:
        return render_template('fromulario_cliente.html', msg='Método HTTP incorrecto')



#Form Dan - Form References
def get_categorias():
    conexion_MySQLdb = connectionBD()
    categorias = []

    if conexion_MySQLdb:
        cursor = conexion_MySQLdb.cursor(dictionary = True)
        sql = "SELECT idCate, nomCate FROM categorias"
        cursor.execute(sql)
        categorias = cursor.fetchall()
        cursor.close()
        conexion_MySQLdb.close()

    return categorias

def get_telas():
    conexion_MySQLdb = connectionBD()
    telas = []
    
    if conexion_MySQLdb:
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        sql = "SELECT idTela, nomTela FROM tela"
        cursor.execute(sql)
        telas = cursor.fetchall()
        cursor.close()
        conexion_MySQLdb.close()
        
    return telas


@app.route('/refere')
def iniciorss():
    categorias = get_categorias()  # Fetch categories from the database
    telas = get_telas()
    return render_template('ref.html', categorias=categorias, telas=telas)


def get_cate1():
    conexion_MySQLdb = connectionBD()
    cateId = []

    if conexion_MySQLdb:
        cursor = conexion_MySQLdb.cursor(dictionary = True)
        sql = "SELECT idCate FROM categorias"
        cursor.execute(sql)
        cateId = cursor.fetchall()
        cursor.close()
        conexion_MySQLdb.close()

    return cateId

def get_cate2():
    conexion_MySQLdb = connectionBD()
    cateNom = []

    if conexion_MySQLdb:
        cursor = conexion_MySQLdb.cursor(dictionary = True)
        sql = "SELECT nomCate FROM categorias"
        cursor.execute(sql)
        cateNom = cursor.fetchall()
        cursor.close()
        conexion_MySQLdb.close()

    return cateNom


@app.route('/test_catalogo')
def test15():
    cateId = get_cate1()
    cateNom = get_cate2()
    return render_template('test_categorias_catalogo.html', cateId=cateId,cateNom=cateNom)


@app.route('/refere')
def inicior():
    return render_template('ref.html')
@app.route('/refere', methods=['GET', 'POST'])
def registrar_ref():
    msg = ""
    if request.method == 'POST':
        idCate = request.form['idCate'];
        nomRef= request.form['nomRef'];
        precioRef = request.form['precioRef'];
        descripcionRef = request.form['descripcionRef'];
        idTela = request.form['idTela'];
        img = request.form['img'];
        conexion_MySQLdb = connectionBD()

        if conexion_MySQLdb:
            cursor = conexion_MySQLdb.cursor(dictionary = True)
            sql = "INSERT INTO referencia (idCate,nomRef,precioRef,descripcionRef,idTela,img) VALUES (%s,%s,%s,%s,%s,%s)"
            valores = (idCate,nomRef,precioRef,descripcionRef,idTela,img)
            cursor.execute(sql, valores)
            conexion_MySQLdb.commit()
            cursor.close()
            conexion_MySQLdb.close()
            msg = 'Referencia registrada con éxito'
            print(cursor.rowcount, "Registro insertado")
            print("1 Registro insertado, id", cursor.lastrowid)
        else:
            msg = 'Error en la conexión a la base de datos'

        return render_template('ref.html', msg='Successfully')
    else:
        return render_template('ref.html', msg='Método HTTP incorrecto')



@app.route('/test_catalogo')
def testCata():
    return render_template('test_categorias_catalogo.html')



if __name__== '__main__':
    app.run(debug=True,port=5000)