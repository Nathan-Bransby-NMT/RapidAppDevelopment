from src import *
from threading import Thread

def main() -> None:
    """The main task."""
    app = App()
    return app.mainloop()


if __name__ == '__main__':
    Thread(target=main()).run()
