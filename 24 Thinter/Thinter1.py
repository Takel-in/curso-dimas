""" 
    Intefaces fráficas con Tkinter
    Conceptos básicos.

    Para linus: sudo apt-get install python3-tkinter

    Tkinter funciona mediante widgets. Los widgets son elementos predetinidos 
    que podemos ir incrustando en nuestra aplicación.
    Por ejemplo botón, imput de texto....

    Colores: '#00a8e80
    Fuente: curier,25
"""
import tkinter as tk  #Lo renombramos por acortar un poco el nombre.

app = tk.Tk() #Instancia del obj principal
palabra = tk.StringVar(app) #Es una variable que podemos utilizar dentro de la aplicación.
entrada = tk.StringVar(app)


app.geometry("300x600") # W*H Dimensiones de la ventana Anchura por Altura.
app.configure(background="black")#fondo
tk.Wm.wm_title(app, "Título ventana") #LLamamo al Módulo tk, Windows Manager Wm, propietada del título de la ventana y le pasamos nuestra aplciación y el texto.

def saludar():
    print("Hola" + entrada.get())  #entrada lo rellenamos en el objeto Entrey


def cambiarPalabra():
    palabra.set("Ponermos una text" + entrada.get())

#Para añadir cualquier widget suelen ser dos pasos. 
#1ª lo que queremos.
tk.Button(app, # Donde  donde lo incustamos.
          text="Pulsame 1",
          font =("Courier", 14),
          bg="#00a8e8",
          fg="white",
          command= saludar    #Se pueden usar lambda para hacer la función.
            # Como se tiene que incrustar.
          ).pack(
              fill=tk.BOTH, #Ocupe todo lo que puede a lo acho y alto.
              expand=True #Si se redefine el tamaño que lo acepte.
          )

tk.Button(app, # Donde  donde lo incustamos.
          text="Pulsame 2",
          font =("Courier", 14),
          bg="#00a8e8",
          fg="white",
          command= cambiarPalabra    #Se pueden usar lambda para hacer la función.
            # Como se tiene que incrustar.
          ).pack(
              fill=tk.BOTH, #Ocupe todo lo que puede a lo acho y alto.
              expand=True #Si se redefine el tamaño que lo acepte.
          )

tk.Label(app, 
            text="Soy una etiquta",
            textvariable=palabra,
            fg = "white",
            bg = "black",
            justify="center"
        ).pack(
              fill=tk.BOTH, #Ocupe todo lo que puede a lo acho y alto.
              expand=True #Si se redefine el tamaño que lo acepte.
          )

tk.Entry(app, 
            fg = "white",
            bg = "black",
            justify = "center",
            textvariable = entrada
        ).pack(
              fill=tk.BOTH, #Ocupe todo lo que puede a lo acho y alto.
              expand=True #Si se redefine el tamaño que lo acepte.
          )

app.mainloop() #Se encarga de refescar constantemente la aplicación.

