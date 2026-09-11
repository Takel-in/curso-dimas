import tkinter as tk
from controller import Controller
from screens.homeScreen import HomeScreen
from screens.addTestScreen import AddTestScreem

from style import styles

class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Examenes de Programación")
        self.controller = Controller()

        self.container = tk.Frame(self)  #Frame Principal
        self.container.pack(
            side = tk.TOP,
            fill=tk.BOTH,
            expand=True
        )

        self.container.configure(
            background=styles.BACKGROUND
        )
        # 1 indica los grande que es respecto al resto de columnas (en este caso ocupa lo mismo.)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        #Definimos nuestro diccionario de pantalla.
        self.frame = {}
        pantallas = (HomeScreen, AddTestScreem, )  
        for f in pantallas:
            frame = f(self.container, self)
            self.frame[f] = frame
            frame.grid(row =0, column=0, sticky=tk.NSEW) #Esto ocupa toda la pantalla.

        self.show_frame(HomeScreen)


    def show_frame(self, frame_class):
        frames = self.frame[frame_class]
        frames.tkraise()

    # Aqui empiezan las transiciones de pantallas
    def homeToCreate(self):
        self.show_frame(AddTestScreem)

