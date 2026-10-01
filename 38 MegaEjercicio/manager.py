import tkinter as tk
from controller import Controller
from screens.homeScreen import HomeScreen
from screens.addTestScreen import AddTestScreem
from screens.updateTestScreen import UpdateTestScreen
from screens.selectTestScreen import SelectTestScreen
from screens.executeTestScreen import ExecuteTestScreen
from screens.testFinishedScreen import TestFinishedScreen
from screens.deleteTestScreen import DeleteTestScreen
from style import styles

class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Examenes de Programación")
        self.controller = Controller()
        self.selected_test = ""
        self.num_questions = 0
        self.num_aciertos =0
        self.questions = ""


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
        pantallas = (HomeScreen, AddTestScreem, UpdateTestScreen, SelectTestScreen, ExecuteTestScreen, TestFinishedScreen, DeleteTestScreen)  
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

    def homeToUpdate(self):
        # Siempre que vayamos a esta pantalla necesitamos cargar los test
        # de nuevo por si se han modificado.
        new_options = self.get_test_names()
        self.frame[UpdateTestScreen].options.update_options(new_options)
        self.show_frame(UpdateTestScreen)

    def homeToSelect(self):
        # Siempre que vayamos a esta pantalla necesitamos cargar los test
        # de nuevo por si se han modificado.
        new_options = self.get_test_names()
        self.frame[SelectTestScreen].options.update_options(new_options)
        self.show_frame(SelectTestScreen)

    def selectToExecute(self):
        self.selected_test = self.frame[SelectTestScreen].options.selected.get()
        self.get_test()
        self.show_frame(ExecuteTestScreen)

    def executeToFinish(self):
        self.frame[TestFinishedScreen].results.set(
            f"{self.num_aciertos} / {self.num_questions}"
        )
        self.num_aciertos=0
        self.num_questions=0
        self.show_frame(TestFinishedScreen)

    def homeToDelete(self):
        new_options = self.get_test_names()
        self.frame[DeleteTestScreen].options.update_options(new_options)
        self.show_frame(DeleteTestScreen)

    # Aqui empiezan los métodos de la BBDD
    def get_test_names(self):
        return self.controller.get_test_names()

    def add_question(self, test_name, question_text, question_choices, correct_choice):
        self.controller.add_question( test_name, question_text, question_choices, correct_choice  )

    def get_test(self):
        if self.selected_test != "" :
            _questions = self.controller.get_test_questions(self.selected_test)
            self.questions = iter(_questions)
            self.frame[ExecuteTestScreen].init_widgets(next(self.questions))

    def deleteTest(self, test_name):
        self.controller.deleteTest(test_name)