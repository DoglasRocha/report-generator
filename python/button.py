from tkinter import Button as tk_button

class Button(tk_button):
    
    def __init__(self, mainframe, row: int, column: int, background="#0F0E0E", foreground="#EEEEEE", *args, **kwargs):
        super().__init__(mainframe, background=background, foreground=foreground, *args, **kwargs)
        self.grid(row=row, column=column)