import tkinter as tk
import tkinter.messagebox
from style import styles
from components.mainMenu import MainMenu
from components.SelectOption import SelectOption

class DeleteTestScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)
        self.option_list = self.manager.get_test_names()
        self.init_widgets()

    def init_widgets(self):
        tk.Label(
            self,
            text = "Selecciona el test a eliminar",
            justify = tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        self.options = SelectOption(
            self,
            self.manager,
            self.option_list
        )

        self.options.pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text="Eliminar Test",
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT,
            **styles.STYLE,
            command = lambda :self.deleteTest()
        ).pack(
            **styles.PACK
        )

        MainMenu(
            self,
            self.manager
        ).pack(
            **styles.PACK
        )

    def deleteTest(self):
        _test_name = self.options.selected.get()
        tk.messagebox.showinfo(
            title = "ATENCION",
            message=f"Seguro que quieres eleminar {_test_name}?"
        )

        self.manager.deleteTest(self.options.selected.get())

        tk.messagebox.showinfo(
            title = "REALIZADO",
            message=f"Eliminado el test {_test_name}?"
        )

        #Actualizamos el menú de opcioens.
        test_names = self.manager.get_test_names()
        self.options.update_options(test_names)