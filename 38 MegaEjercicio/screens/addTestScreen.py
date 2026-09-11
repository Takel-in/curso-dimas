import tkinter as tk
import tkinter.messagebox 
from sqlite3 import ProgrammingError
from style import styles
from components.mainMenu import MainMenu

class AddTestScreem(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.configure(background=styles.BACKGROUND)
        self.manager = manager
        self.init_widgets()

    def init_widgets(self):
        tk.Label(
            self,
            text = "Introducie el nombre del nuevo testo",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )


        self.test_entry = tk.Entry(
            self,
            justify=tk.CENTER,
            **styles.STYLE
        )

        self.test_entry.pack(
            **styles.PACK
        )

        self.test_entry.bind("<Return>", self.add_test)

        MainMenu(
            self, 
            self.manager
            ).pack(
                **styles.PACK
            )

    def add_test(self, event):
        self.test_name = self.test_entry.get()
        if self.test_name == "":
            tk.messagebox.showinfo (
                title="ERRO",
                message="El nombre dle test no puede estar vacío"
            )
        else:
            try:
                self.manager.controller.create_empty_test(self.test_name)
                tk.messagebox.showinfo (
                    title="SUCCESS",
                    message=f"El test {self.test_name} ha sido creado"
                )
            except ProgrammingError:
                tk.messagebox.showinfo (
                    title="ERROR",
                    message=f"Ya existe un test con este nombre, prueba con otro."
                )
            finally:
                print (self.test_name)
    