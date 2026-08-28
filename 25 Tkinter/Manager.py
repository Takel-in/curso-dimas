# TKinter2
# Generamos un juego de ejemplo el YO NUNCA.

import tkinter as tk
from constantes import style
from screens import *

class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Yo nunca: The Game")
        container = tk.Frame(self)  #Decimos que este frame es nuestro parent
        container.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand=True
        )
        container.configure(bg=style.BACKGROUND)
        container.grid_columnconfigure(0, weight=1) # #Indice de la columna, Lo que ocupa respecto a las demas // pero solo tiene una
        container.grid_rowconfigure(0,weight=1) #Indice de la fila, Lo que ocupa respecto a las demas // pero solo tiene una

        self.frames = {}

        for f in (Home, Game):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)
        self.show_frame(Home) #Indicamos que la primera vez muestre la pantalla principal.


    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise() #La ponermos delante de todo.



