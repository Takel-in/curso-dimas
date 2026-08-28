# Pantalla Home
import tkinter as tk
from constantes import style


class Home(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg=style.BACKGROUND)
        self.controller = controller

    # A partir de aquí constrimos nuestra pantalla.
        self.gameMode = tk.StringVar(self, value = "Normal") 
        self.initWidgets() #Nos cremoas una función para colocar todos los elementos e inicializarlos.

    def initWidgets(self):

        #Cartel de bienvenida.
        tk.Label(self,
                 text="YO NUNCA: THE GAME",
                 justify=tk.CENTER,
                 **style.STYLE  # Esto desempaqueta el diccionario y le pasa todo lo que pone en STYLE.
                  ).pack( # Para que lo posiciones dentro de la pantalla.
                      side = tk.TOP,
                      fill = tk.BOTH,
                      expand=True,
                      padx = 22,
                      pady = 11

                  )

        # Introducimos otro Frame que o ocupe todo sino un poco más pequeño.
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background=style.BACKGROUND)
        optionsFrame.pack(
                        side = tk.TOP,
                        fill = tk.BOTH,
                        expand=True,
                        padx = 22,
                        pady = 11      
        )






class Game(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg=style.BACKGROUND)
        self.controller = controller