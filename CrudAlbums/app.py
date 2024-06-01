#hacer las importaciones necesarias para la práctica
#para renderizar o generar la vista se necesita el render_template
from flask import Flask, request, render_template
#agregar una importación de lo que se necesite de la base de dato
from flask_mysqldb import MySQL

#declara una variable
app=Flask(__name__)

#da de alta las variables de la configuración de la bd
app.config['MYSQL_HOST']='localhost'
#da de alta lo del usuario con el que te conectas a la bd
app.config['MYSQL_USER']='root'

app.config['MYSQL_PASSWORD']=''
#contraseña de la bd que por lo general viene vacia
app.config['MYSQL_DB']='bdflask'

#crear una variable que se va a usar para la conexion a la bd
mysql= MySQL(app)

#crear una ruta para ejecutar la vista index

@app.route('/')
def index():
    return render_template('index.html')

#crear una función para mandar los datos al momento de pulsar el boton.
@app.route('/guardarAlbum', methods=['POST'])
def guardarAlbum():
    if request.method == 'POST':
        titulo= request.form['txtTitulo']
        artista=request.form['txtArtista']
        anio=request.form['txtAnio']
        print(titulo,artista,anio)
        return 'Datos recibidos en el server'



#Manejo de excepciones para rutas 
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: No encontré nada'
#ejecutar el proyecto
if __name__ == '__main__':
    app.run(port=3000, debug=True) 
    #debug nos ayuda principalmente a las refrescar en caso de que haya algún cambio