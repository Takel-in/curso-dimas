import tkinter as tk
from style import styles

class MainMenu(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager=manager
        self.configure(
            background=styles.BACKGROUND
        )
        self.init_widgets()

    def init_widgets(self):
        tk.Button(
            self,
            text="HACER UN TEST",
            command=lambda: self.manager.homeToSelect(),
            **styles.STYLE,
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text="CREAR UN TEST",
            command=lambda: self.manager.homeToCreate(),
            **styles.STYLE,
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text="EDITAR UN TEST",
            command=lambda: self.manager.homeToUpdate(),
            **styles.STYLE,
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text="ELIMINAR UN TEST",
            command=lambda: self.manager.homeToDelete(),
            **styles.STYLE,
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )
