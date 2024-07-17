import tkinter as tk

type Calculation = tuple[int | None, str | None, int | None]

DEFAULT_VALUE: Calculation = (1, '+', 1)


class App(tk.Tk):
    """The main application class."""

    log: list[Calculation] = []
    _display_value: Calculation = DEFAULT_VALUE

    def __init__(self) -> None:
        super().__init__()
        self.geometry('600x800')
        self.screen = tk.Label(self, anchor='n', justify='center', borderwidth=2, fg='#ffffff', bg='#101010', relief='raised')
        self.__build_display()

    def __build_display(self) -> None:
        """Internal Function that is called to build the UI."""
        self.screen['text'] = self.display_value
        self.screen.grid(column=0, row=0, columnspan=3)
        self.__update_display()

    def __update_display(self) -> None:
        self.screen.update()

    @property
    def display_value(self) -> str:
        """Return the value of the display."""
        if self._display_value[2] != None:
            match self._display_value[1]:  # This is just temporary, until we have functions
                case '+':
                    total = self._display_value[0] + self._display_value[2]
                case '-':
                    total = self._display_value[0] - self._display_value[2]
                case '*':
                    total = self._display_value[0] * self._display_value[2]
                case '/':
                    total = self._display_value[0] / self._display_value[2]
                case _:
                    total = None
        _sum = ''.join([str(x) for x in self._display_value if x is not None]) + f' = {total}' if total is not None else ""
        return _sum