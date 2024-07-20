from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mysqldb import MySQL
#se utiliza para enviar archivos desde un directorio específico en el servidor
from flask import send_from_directory 
#según el video este es para evitar archivos dañados
from werkzeug.utils import secure_filename
# segun el video proporciona una forma de usar funcionalidades dependientes del sistema operativo
import os
#se usa como una constante que especifica el directorio donde se guardarán los archivos subidos
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'
app.config['UPLOAD_FOLDER'] = 'uploads'  # Est carpeta es para almacenar imágenes
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'png'} #esta es para las extensiones de las imagenes permitidas
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

# De acuerdo al video esta función que me sirve para verificar la extensión del archivo
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM albums')
        consultaA = cursor.fetchall()
        return render_template('index.html', albums=consultaA)
    except Exception as e:
        print(e)

@app.route('/guardarAlbum', methods=['POST'])
def guardarAlbum():
    if request.method == 'POST':
        Ftitulo = request.form['txtTitulo']
        Fartista = request.form['txtArtista']
        Fanio = request.form['txtAnio']
        # nos ayuda a verificar las imagenes que si sean del formato
        file = request.files['file']
        if file and allowed_file(file.filename): #Verifica si el nombre del archivo tiene una extensión permitida
            filename = secure_filename(file.filename)# para asegurar que el nombre del archivo sea seguro para almacenar en el sistema de archivos.
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))# guarda el archivo en la ruta especificada.
            portada_url = url_for('uploaded_file', filename=filename) #crea una URL para la ruta que sirve archivos subidos. 
        else:
        #en caso de que no sea se manda un mensaje de alerta
            flash('Tipo de archivo no permitido. Solo se permiten archivos .jpg y .png.')
            return redirect(url_for('index'))
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO albums (titulo, artista, anio, portada) VALUES (%s, %s, %s, %s)', (Ftitulo, Fartista, Fanio, portada_url))
        mysql.connection.commit()
        
        flash('Álbum guardado correctamente')
        return redirect(url_for('index'))

@app.route('/editar/<id>')
def editar(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM albums WHERE id_album = %s', [id])
    albumE = cur.fetchone()
    return render_template('editar.html', album=albumE)

@app.route('/ActualizarAlbum/<id>', methods=['POST'])
def ActualizarAlbum(id):
    if request.method == 'POST':
        Ftitulo = request.form['txtTitulo']
        Fartista = request.form['txtArtista']
        Fanio = request.form['txtAnio']
        
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],  filename))
            portada_url = url_for('uploaded_file', filename=filename)
        else:
            # Mantener la portada anterior si no se proporciona un nuevo archivo
            cur = mysql.connection.cursor()
            cur.execute('SELECT portada FROM albums WHERE id_album = %s', [id])
            portada_url = cur.fetchone()[0]
        
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE albums SET titulo = %s, artista = %s, anio = %s, portada = %s WHERE id_album = %s', (Ftitulo, Fartista, Fanio, portada_url, id))
        mysql.connection.commit()
        
        flash('Álbum editado correctamente')
        return redirect(url_for('index'))

@app.route('/EliminarAlbum/<id>')
def EliminarAlbum(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM albums WHERE id_album = %s', [id])
    mysql.connection.commit()
        
    flash('Álbum eliminado correctamente')
    return redirect(url_for('index'))

#definimos una nueva ruta que nos permite a los archivos ya subidos 
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],  filename)

# Manejo de excepciones para rutas
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: No encontré nada'

# Ejecutar el proyecto
if __name__ == '__main__':
    app.run(port=3000, debug=True)
