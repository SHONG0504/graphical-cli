import os, sys

from tkinter import *

class Display(Tk):
    def __init__(self):
        super().__init__()
        self.title("Graphical CLI")

        self.current_dir = Label(self, text=home)
        self.current_dir.place(relx=0, rely=0, anchor=NW)

        self.mainloop()

if __name__ == "__main__":
    home = os.path.expanduser('~')

    display = Display()