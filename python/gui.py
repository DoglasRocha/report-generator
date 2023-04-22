from tkinter import Tk, Frame, Entry, filedialog
from button import Button
from label import Label
from oop_report_generator import ReportGenerator
from os.path import exists

class GUI(Tk):
    
    def __init__(self):
        # create generator and text variables
        self.report_generator = ReportGenerator()
        self._output_dir = ""
        
        # init and config window
        super().__init__()
        self.title("Gerador de Relatórios")
        mf = Frame(self, padx=10, pady=10, background="#0F0E0E")
        mf.pack()
        
        # First level
        Label(mf, 1, 2, text="Gerador de Relatório", font=('Arial', '22'))
        Label(mf, 2, 1) # spacer
        
        # Second Level
        Label(mf, 3, 1, text="Arquivo de Atividades: \t")
        self._activities_label = Label(mf, 3, 2, text="Nenhum arquivo aberto")
        Button(mf, 3, 3, text="Abrir arquivo de Atividades", command=self.get_activities_file_name)
        Label(mf, 4, 1) # spacer
        
        # Third Level
        Label(mf, 5, 1, text="Abrir arquivo template de relatório: \t")
        self._template_label = Label(mf, 5, 2, text="Nenhum arquivo aberto")
        Button(mf, 5, 3, text="Abrir arquivo template de relatório", command=self.get_template_file_name)
        Label(mf, 6, 1) # spacer
        
        # Fourth Level
        Label(mf, 7, 1, text="Diretório de destino: \t")
        self._output_label = Label(mf, 7, 2, text="Nenhum diretório aberto")
        Button(mf, 7, 3, text="Abrir diretório de destino", command=self.get_output_dir)
        Label(mf, 8, 1) # spacer
        
        # Fifth Level
        self._label4 = Label(mf, 9, 1, text="Nome do relatório gerado: \t")
        self._text1 = Entry(mf, background="#0F0E0E", foreground="#EEEEEE")
        self._text1.grid(column=3, row=9)
        Label(mf, 10, 1) # spacer
        
        # Sixth Level
        Button(mf, 11, 2, text="Gerar relatório", command=self.generate_report)
        Label(mf, 12, 1) # spacer
        
        # Seventh Level
        self._messages_label = Label(mf, 13, 2)
        
    def get_activities_file_name(self):
        filename = filedialog.askopenfilename(initialdir=".",
                                              title="Selecione o arquivo de atividades", 
                                              filetypes=(("Excel files", "*.xlsx"),))
        (
            self
            ._activities_label
            .configure(
                text="Nenhum arquivo aberto" if filename == "" else filename.split("/")[-1]
            )
        )
        
        if (exists(filename)):
            self.report_generator.set_activities_table_path(filename)
        
    def get_template_file_name(self):
        filename = filedialog.askopenfilename(initialdir=".",
                                              title="Selecione o template de relatório", 
                                              filetypes=(("Word files", "*.docx"),))
        (
            self
            ._template_label
            .configure(
                text="Nenhum arquivo aberto" if filename == "" else filename.split("/")[-1] 
            )
        )
        
        if (exists(filename)):
            self.report_generator.set_report_template_path(filename) 
            
    def get_output_dir(self):
        output_dir = filedialog.askdirectory(initialdir=".",
                                             title="Selecione a pasta de destino")
        
        (
            self
            ._output_label
            .configure(
                text="Nenhum diretório aberto" if output_dir == "" else output_dir.split("/")[-1] + "/"
            )
        )
        
        if (exists(output_dir)):
            self._output_dir = output_dir
            
    def paths_exist(self):
        return all(
            [exists(self.report_generator.get_activities_table_path()),
            exists(self.report_generator.get_report_template_path()),
            exists(self._output_dir)]
        )
            
    def generate_report(self):
        if self.paths_exist():
            output_file_name = self._text1.get()
            output_file_name = "novo_relatorio" if output_file_name == "" else output_file_name
            output_file_name = output_file_name if ".docx" == output_file_name[-5:] else output_file_name + ".docx"
            
            self.report_generator.set_new_report_path(self._output_dir + "/" + output_file_name)
            self.report_generator.generate_report()
            self._messages_label.configure(text="Relatório gerado com sucesso!", foreground="#8B9A46")
        else:
            self._messages_label.configure(text="Relatório não gerado. Verifique os arquivos selecionados",
                                           foreground="#541212")
            
        

GUI().mainloop()