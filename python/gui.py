from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from oop_report_generator import ReportGenerator

class GUI(Tk):
    
    def __init__(self):
        self.report_generator = ReportGenerator()
        self._output_dir = ""
        self._output_file_name = ""
        
        super().__init__()
        self.title("Gerador de Relatórios")
        self._mf = Frame(self, padding=10)
        self._mf.pack()
        
        self._label1 = Label(self._mf, text="Arquivo de Atividades: \t")
        self._label1.grid(column=1, row=1)
        
        self._button1 = Button(self._mf, text="Abrir arquivo de Atividades", command=self.get_activities_file_name)
        self._button1.grid(column=3, row=1)
        
        Label(self._mf).grid(row=2)
        
        self._label2 = Label(self._mf, text="Abrir arquivo template de relatório: \t")
        self._label2.grid(column=1, row=3)
        
        self._button2 = Button(self._mf, text="Abrir arquivo template de relatório", command=self.get_template_file_name)
        self._button2.grid(column=3, row=3)
        
        Label(self._mf).grid(row=4)
        
        self._label3 = Label(self._mf, text="Diretório de destino: \t")
        self._label3.grid(column=1, row=5)
        
        self._button3 = Button(self._mf, text="Abrir diretório de destino", command=self.get_output_dir)
        self._button3.grid(column=3, row=5)
        
        Label(self._mf).grid(row=6)
        
        self._label4 = Label(self._mf, text="Nome do relatório gerado: \t")
        self._label4.grid(column=1, row=7)
        
        self._text1 = Entry(self._mf)
        self._text1.grid(column=3, row=7)
        
        Label(self._mf).grid(row=8)
        
        Button(self._mf, text="Gerar relatório", command=self.generate_report).grid(column=2, row=9)
        
    def get_activities_file_name(self):
        filename = filedialog.askopenfilename(initialdir=".",
                                              title="Selecione o arquivo de atividades", 
                                              filetypes=(("Excel files", "*.xlsx"),))
        self._label1.configure(text=f'Arquivo de Atividades: {"Nenhum arquivo aberto" if filename == "" else filename.split("/")[-1]}\t')    
        
        if (len(filename) > 5):
            self.report_generator.set_activities_table_path(filename)
        
    def get_template_file_name(self):
        filename = filedialog.askopenfilename(initialdir=".",
                                              title="Selecione o template de relatório", 
                                              filetypes=(("Word files", "*.docx"),))
        self._label2.configure(text=f'Arquivo Template de relatório: {"Nenhum arquivo aberto" if filename == "" else filename.split("/")[-1]}\t')   
        
        if (len(filename) > 5):
            self.report_generator.set_report_template_path(filename) 
            
    def get_output_dir(self):
        output_dir = filedialog.askdirectory(initialdir=".",
                                             title="Selecione a pasta de destino")
        self._label3.configure(text=f'Diretório de destino: {"Nenhum diretório aberto" if output_dir == "" else output_dir.split("/")[-1]}\t')  
        
        if (len(output_dir) > 5):
            self._output_dir = output_dir
            
            
    def generate_report(self):
        output_file_name = "novo_relatorio.docx" if self._text1.get() == "" else f'{self._text1.get()}.docx'
        self.report_generator.set_new_report_path(self._output_dir + "/" + output_file_name)
        self.report_generator.generate_report()
            
    

'''root = Tk()
root.title("Gerador de Relatórios")
frame = Frame(root, padding=10)
frame.pack()

l = Label(frame, text="Hello World")
l.pack()
Button(frame, text="Quit", command=getFileName).pack()
root.mainloop()'''

GUI().mainloop()