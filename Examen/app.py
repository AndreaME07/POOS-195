from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>HOME holis profe</h1>"

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        return f"<h2>Nombre: {nombre}, Edad: {edad}</h2>"
    return render_template('formulario.html')

@app.route('/numeroalcuadrado/<int:num>')
def numeroalcuadrado(num):
    return f"<h2>El cuadrado de {num} es: {num*num}</h2>"

@app.errorhandler(404)
def not_found_error(error):
    return "<h1>Ruta no encontrada. Por favor, verifica la URL ingresada.</h1>", 404

if __name__ == '__main__':
    app.run(debug=True)