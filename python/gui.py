from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

class GUI(Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Gerador de Relatórios")
        self._mf = Frame(self, padding=100)
        self._mf.pack()
        
        self._label1 = Label(self, text="Arquivo: ")
        self._label1.pack()
        
        self._button1 = Button(self, text="Abrir arquivo", command=self.get_file_name)
        self._button1.pack()
        
    def get_file_name(self):
        filename = filedialog.askopenfilename(initialdir=".",
                                     title="aaa")
        self._label1.configure(text=f'Arquivo: {"Nenhum arquivo aberto" if filename == "" else filename}')    

'''root = Tk()
root.title("Gerador de Relatórios")
frame = Frame(root, padding=10)
frame.pack()

l = Label(frame, text="Hello World")
l.pack()
Button(frame, text="Quit", command=getFileName).pack()
root.mainloop()'''

GUI().mainloop()