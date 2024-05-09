
import tkinter as tk
from tkinter import messagebox
from Resta import *

def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = resta_numeros(num1, num2)
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "No se pueden ingresar letras. Por favor, ingrese solo números.")
    else:
        messagebox.showinfo("Información", "Operación realizada con éxito.")

ventana = tk.Tk()
ventana.title("Resta de Números")
ventana.geometry("400x200")


label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack()
entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack()
entry_num2 = tk.Entry(ventana)
entry_num2.pack()

button_restar = tk.Button(ventana, text="Restar", command=restar)
button_restar.pack()

ventana.mainloop()
