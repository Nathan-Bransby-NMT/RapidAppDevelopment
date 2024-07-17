import tkinter as tk

type Calculation = tuple[int, str, int]


class App(tk.Tk):
    """The main application class."""

    log: list[Calculation] = []
    display_value = tk.IntVar(0)

    def __init__(self) -> None:
        super().__init__()
        self.geometry('600x800')
        self.screen = tk.Label(textvariable=str(self.display_value))
        self.__build_display()

    def __build_display(self) -> None:
        """Internal Function that is called to build the UI."""
        self.screen.grid(column=0, row=0, columnspan=3)
