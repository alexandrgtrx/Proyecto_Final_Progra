import tkinter as tk
import random
#import numpy as np //aun no esta agregado, pero se utilizara


def boton_clicado():
    print("Has clicado un botón")

def generar_numero():
    return random.randint(0, 11)

def crear_matriz():
    global n
    n = int(entry.get())

    for i in range(n):
        for j in range(n):
            numero = generar_numero()
            boton = tk.Button(frame, text=str(numero), command=boton_clicado, width=2,height=2)
            boton.grid(row=i, column=j)

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Matriz Aritmetica")
ventanaPrincipal.geometry("450x450")
ventanaPrincipal.resizable(0,0)
ventanaPrincipal.iconbitmap("Logo-Meso-Color.ico")

frame = tk.Frame(ventanaPrincipal)
frame.pack()

label = tk.Label(ventanaPrincipal, text="Ingrese el tamaño de la matriz:")
label.pack()

entry = tk.Entry(ventanaPrincipal)
entry.pack()

boton = tk.Button(ventanaPrincipal, text="Crear matriz", command=crear_matriz)
boton.pack()

ventanaPrincipal.mainloop()