class Restar:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def resta_numeros(self):
        resultado = self.num1 - self.num2
        if resultado < 0:
            return "El resultado es negativo."
        else:
            return f"El resultado de la resta es: {resultado}"
