import tkinter as tk


class App(tk.Tk):
    """The main application class."""

    log = []

    def __init__(self) -> None:
        super().__init__()
        self.geometry('600x800')

    
