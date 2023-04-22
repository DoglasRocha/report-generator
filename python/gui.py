from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

def getFileName():
    filename = filedialog.askopenfilename(initialdir=".",
                                     title="aaa")
    l.configure(text=f'Arquivo: {"Nenhum arquivo aberto" if filename == None else filename}')
    

root = Tk()
root.title("Gerador de Relatórios")
frame = Frame(root, padding=10)
frame.pack()

l = Label(frame, text="Hello World")
l.pack()
Button(frame, text="Quit", command=getFileName).pack()
root.mainloop()