#Hacer un hola mundo con flask
#Hacer las importaciones necesarias, en este caso sería de flask
from flask import Flask

#declara una variable
app=Flask(__name__)

if __name__ == '__main__':
    app.run(port=3000, debug=True) 
    #debug nos ayuda principalmente a las refrescar en xcaso de que haya algún cambio