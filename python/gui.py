from tkinter import Tk, Frame, Entry ,filedialog
from tkinter import Label as tkLabel
from button import Button
from label import Label
from oop_report_generator import ReportGenerator

class GUI(Tk):
    
    def __init__(self):
        # create generator and text variables
        self.report_generator = ReportGenerator()
        self._output_dir = ""
        self._output_file_name = ""
        
        # init and config window
        super().__init__()
        self.title("Gerador de Relatórios")
        mf = Frame(self, padx=10, pady=10, background="#0F0E0E")
        mf.pack()
        
        # First level
        Label(mf, 1, 2, text="Gerador de Relatório", font=('Arial', '22'))
        Label(mf, 2, 1) # spacer
        
        # Second Level
        self._label1 = Label(mf, 3, 1, text="Arquivo de Atividades: \t")
        Button(mf, 3, 3, text="Abrir arquivo de Atividades", command=self.get_activities_file_name)
        Label(mf, 4, 1) # spacer
        
        # Third Level
        self._label2 = Label(mf, 5, 1, text="Abrir arquivo template de relatório: \t")
        Button(mf, 5, 3, text="Abrir arquivo template de relatório", command=self.get_template_file_name)
        Label(mf, 6, 1) # spacer
        
        # Fourth Level
        self._label3 = Label(mf, 7, 1, text="Diretório de destino: \t")
        Button(mf, 7, 3, text="Abrir diretório de destino", command=self.get_output_dir)
        Label(mf, 8, 1) # spacer
        
        # Fifth Level
        self._label4 = Label(mf, 9, 1, text="Nome do relatório gerado: \t")
        
        self._text1 = Entry(mf, background="#0F0E0E", foreground="#EEEEEE")
        self._text1.grid(column=3, row=9)
        Label(mf, 10, 1) # spacer
        
        Button(mf, 11, 2, text="Gerar relatório", command=self.generate_report)
        
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