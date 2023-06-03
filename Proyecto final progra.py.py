import tkinter as tk
import random
#import numpy as np //aun no esta agregado, pero se utilizara
def cuenta_regresiva():
    # Crear la ventana de la cuenta regresiva
    ventana = tk. Tk()
    ventana. title("Cuenta Regresiva")
    ventana. geometría("200x100")

    # Crear una etiqueta para mostrar los segundos restantes
    etiqueta = tk. Label(ventana, font=("Helvetica", 48))
    etiqueta. paquete(pady=20)

    # Inicializar el valor de los segundos en 25
    segundos = 25

    # Función para actualizar la etiqueta con el valor actual de segundos
    def actualizar_etiqueta():
        segundos no locales 
        etiqueta. config(text=str(segundos))
        Si segundos > 0:
            segundos -= 1
            etiqueta. después (1000, actualizar_etiqueta)

    # Llamar a la función para iniciar la cuenta regresiva
    actualizar_etiqueta()

    # Ejecutar el bucle principal de la ventana
    ventana. mainloop()

# Para jecutar la función de cuenta regresiva la llamamos con :
# cuenta_regresiva()


def boton_clicado():
    print("Has clicado un botón")

def generar_numero():
    return random.randint(0, 11)

def crear_matriz():
    global jugador1
    global jugador2
    global n
    n = int(entry3.get())
    jugador1 = (entry1.get())
    jugador2 = (entry2.get())

    for i in range(n):
        for j in range(n):
            numero = generar_numero()
            boton = tk.Button(frame, text=str(numero), command=boton_clicado, width=2,height=2)
            boton.grid(row=i, column=j)
    label = tk.Label(ventanaPrincipal, text= jugador1)
    label.pack()
    label = tk.Label(ventanaPrincipal, text= "VS")
    label.pack()
    label = tk.Label(ventanaPrincipal, text= jugador2)
    label.pack()

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Matriz Aritmetica")
#ventanaPrincipal.geometry("450x450")
ventanaPrincipal.resizable(0,0)
ventanaPrincipal.iconbitmap("Logo-Meso-Color.ico")

frame = tk.Frame(ventanaPrincipal)
frame.pack()

label = tk.Label(ventanaPrincipal, text="Ingrese el nombre del primer jugador:")
label.pack()
entry1 = tk.Entry(ventanaPrincipal)#lectura del nombre del primer jugador 
entry1.pack()
label = tk.Label(ventanaPrincipal, text="Ingrese el nombre del segundo jugador:")
label.pack()
entry2 = tk.Entry(ventanaPrincipal)#lectura del nombre del segundo jugador
entry2.pack()
label = tk.Label(ventanaPrincipal, text="Ingrese el tamaño de la matriz:")
label.pack()
entry3 = tk.Entry(ventanaPrincipal)#lectura del tamaño de la matriz
entry3.pack()

label = tk.Label(ventanaPrincipal, text="Ingrese el tamaño de la matriz:")
label.pack()

boton = tk.Button(ventanaPrincipal, text="Crear matriz", command=crear_matriz)
boton.pack()

ventanaPrincipal.mainloop()
