#Hacer un hola mundo con flask
#Hacer las importaciones necesarias, en este caso sería de flask
from flask import Flask,request


#declara una variable
app=Flask(__name__)

#Ruta simple (ejemplificar la ruta)
@app.route('/')
def principal():
    return 'Hola mundo Flask'

#Ruta Doble (que dos URL lleven a un mismo lugar)
@app.route('/usuario')
@app.route('/saludar')
def saludos():
    return 'Hola Andrea Medina alias Nancy'

#Rutas con parámetros, son aquellas que necesitan la variable o el parametro para ejecutar
#en caso de que se necesite dar un nuevo tipo de dato y se convirta se pone un int o un float
@app.route('/hi/<nombre>')
def hi(nombre):
    return 'Hola'+nombre + '!!!'

#Definición de metodos de trabajo
@app.route('/formulario/', methods=['GET','POST'])
def formulario():
    if request.method == 'GET':
        return 'No es seguro enviar password por GET'
    elif request.method == 'POST':
        return 'Post si es seguro para password'

#Manejo de excepciones para rutas 
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: No encontré nada'

if __name__ == '__main__':
    app.run(port=3000, debug=True) 
    #debug nos ayuda principalmente a las refrescar en caso de que haya algún cambio