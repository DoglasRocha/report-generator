import pandas as pd
from sys import argv
from docxtpl import DocxTemplate
from datetime import date

class ReportGenerator():
    
    def __init__(self):
        self._activities_table_path = ""
        self._report_template_path = ""
        self._new_report_path = ""
        self._activities_table = ""
        self._report_template = ""
        self._weekly_data = {}
        self._hours_sum = []
        self._total_sum = ""
        
    def get_activities_table_path(self) -> str:
        return self._activities_table_path
    
    def set_activities_table_path(self, new_path: str) -> None:
        self._activities_table_path = new_path
        
    def get_report_template_path(self) -> str:
        return self._report_template_path
    
    def set_report_template_path(self, new_path: str) -> None:
        self._report_template_path = new_path
        
    def get_new_report_path(self) -> str:
        return self._new_report_path
    
    def set_new_report_path(self, new_path: str) -> str:
        self._new_report_path = new_path
        
    def __read_activities_table(self) -> None:
        self._activities_table = pd.read_excel(self._activities_table_path)
        
    def __read_report_template(self) -> None:
        self._report_template = DocxTemplate(self._report_template_path)
        
    def __load_data(self) -> None:
        self.__read_activities_table()
        self.__read_report_template()
        
    def __mine_activities(self) -> None:
        all_activities = self._activities_table[['Data', 'Atividades', 'Horas']]
        
        # week
        for i in range(5):
            self._weekly_data[f'week{i}'] = []
            
            # days
            for j in range(5):
                if (i * 5 + j) >= len(all_activities.index):
                    break
                
                day = all_activities['Data'].iloc[i * 5 + j]
                day = '-' if pd.isnull(day) or day == '-' else day.strftime("%d/%m")
                    
                hour = all_activities['Horas'].iloc[i * 5 + j]
                hour = '-' if pd.isnull(hour) or hour == '-' else hour.strftime("%H:%M")
                    
                activity = all_activities['Atividades'].iloc[i * 5 + j]
                
                self._weekly_data[f'week{i}'].append({
                    'date': day, 'activity': activity, 'hours': hour
                })
                
    def __mine_hours_sum(self) -> None:
        for i in range(5):
            self._hours_sum.append(self._activities_table.iloc[6 + i, 5].strftime('%H:%M'))
            
    def __mine_total_sum(self) -> None:
        brute_sum = self._activities_table.iloc[3, 4]
        self._total_sum = f'{brute_sum.hour + brute_sum.day * 24}:{brute_sum.strftime("%M")}'
        
    def __mine_data(self) -> None:
        self.__mine_activities()
        self.__mine_hours_sum()
        self.__mine_total_sum()
                
    def generate_report(self) -> None:
        self.__load_data()
        self.__mine_data()
        
        MONTHS = {
            '1': 'Janeiro',
            '2': 'Fevereiro',
            '3': 'Março',
            '4': 'Abril',
            '5': 'Maio',
            '6': 'Junho',
            '7': 'Julho',
            '8': 'Agosto',
            '9': 'Setembro',
            '10': 'Outubro',
            '11': 'Novembro',
            '12': 'Dezembro'
        }
        today = date.today()
        
        self._report_template.render({
            'weekly_data': self._weekly_data,
            'hours_sum': self._hours_sum,
            'total_sum': self._total_sum,
            'month': MONTHS[str(today.month)],
            'year': today.year,
            'scholarship_number': today.month - 2
        })
        self._report_template.save(self._new_report_path)
                
generator = ReportGenerator()
generator.set_activities_table_path("../Atividades/Atividades Estágio Março_Abril.xlsx")
generator.set_report_template_path("../relatorio_template.docx")
generator.set_new_report_path("../novo_relatorio.docx")

generator.generate_report()
