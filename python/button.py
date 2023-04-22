from tkinter import Button as tk_button

class Button(tk_button):
    def __init__(self, mainframe, row: int, column: int, *args, **kwargs):
        super().__init__(mainframe, *args, **kwargs)
        self.grid(row=row, column=column)