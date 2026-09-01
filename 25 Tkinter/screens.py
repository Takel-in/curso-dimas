# Pantalla Home
import tkinter as tk
from constantes import style, config


class Home(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg=style.BACKGROUND)
        self.controller = controller

    # A partir de aquí constrimos nuestra pantalla.
        self.gameMode = tk.StringVar(self, value = "Normal") 
        self.initWidgets() #Nos cremoas una función para colocar todos los elementos e inicializarlos.

    def move_to_game(self):
        self.controller.mode = self.gameMode.get()
        self.controller.show_frame(Game)



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
        optionsFrame.configure(background=style.COMPONENT)
        optionsFrame.pack(
                        side = tk.TOP,
                        fill = tk.BOTH,
                        expand=True,
                        padx = 22,
                        pady = 11      
        )
        # Ahora introducimos una label y una multiselección de opción en el frame.
        tk.Label(optionsFrame,
                 text="Elige tu modo de juego",
                 justify=tk.CENTER,
                **style.STYLE
        ).pack(
                        side = tk.TOP,
                        fill = tk.X,
                        padx = 22,
                        pady = 11      
        )
        for (key, value) in config.MODES.items():
            tk.Radiobutton (
                optionsFrame,
                text=key + ("🔥" if key == "ATREVIDO" else ""),
                variable=self.gameMode,
                value=value,
                activebackground=style.BACKGROUND,
                activeforeground=style.TEXT,
                **style.STYLE
            ).pack(
                side=tk.LEFT,
                fill=tk.BOTH,
                expand=True,
                padx=5,
                pady=5
            )
        tk.Button(self,
            text="EMPEZAR",
            command = self.move_to_game,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=5,
            pady=5

        )





class Game(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg="red")
        self.controller = controller

    # A partir de aquí constrimos nuestra pantalla.
        self.gameMode = tk.StringVar(self, value = "Normal") 
        self.currentQuestion = tk.StringVar(self, value = "PREPARADOS, LISTOS, DALE... ")
        self.fichero = None
        self.initWidgets() #Nos cremoas una función para colocar todos los elementos e inicializarlos.

    def update_question (self):
        self.mode = self.controller.mode
        #Si nunca hemos habierto un fichero o el nombre no coincide con el modo de juego abrimos el que corresponde.
        if (self.fichero == None) or (self.controller.mode.lower() not in self.fichero.name.lower()): #
            self.fichero = open(f'./25 Tkinter/ficheros/{self.mode}.txt', 'r', encoding='utf-8')
        tmp = self.fichero.readline()
        if tmp != "":
            self.currentQuestion.set(tmp)
        else:
            self.currentQuestion.set("ya hemos leido todas las preguntas empezamos")
            #Lo logico no es hacer esto sino mover el cursos al principio.
            self.fichero.close()
            self.fichero = open(f'./25 Tkinter/ficheros/{self.mode}.txt', 'r', encoding='utf-8')
        


    def initWidgets(self):

        #Cartel de bienvenida.
        tk.Label(self,
                 text="YO NUNCA.....",
                 justify=tk.CENTER,
                 **style.STYLE  # Esto desempaqueta el diccionario y le pasa todo lo que pone en STYLE.
                  ).pack( # Para que lo posiciones dentro de la pantalla.
                      side = tk.TOP,
                      fill = tk.BOTH,
                      expand=True,
                      padx = 22,
                      pady = 11

                  )

            # Ahora introducimos una label y una multiselección de opción en el frame.
        tk.Label ( self,
                 text="PREPRADOS, LISTOS, DALE ...",
                 textvar = self.currentQuestion,
                 justify=tk.CENTER,
                **style.STYLE
        ).pack(
                        side = tk.TOP,
                        fill = tk.X,
                        padx = 22,
                        pady = 11      
        )

        tk.Button(self,
            text="SIGUIENTE ->",
            command = self.update_question,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=5,
            pady=5
        )

        tk.Button(self,
            text="<- HOME",
            command = lambda : self.controller.show_frame(Home),
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=5,
            pady=5
        )
