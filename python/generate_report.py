import pandas as pd
from sys import argv, exit
from docxtpl import DocxTemplate
from os.path import exists
from datetime import date

if (len(argv) != 4):
    print("Incorrect usage. Correct usage:")
    print("./generate_report.py activities_table.xlsx report_template.docx generated_report_name.docx")
    exit(1)

def read_table(table_path):
    try:
        activities_table = pd.read_excel(table_path)
        return activities_table
    except (FileNotFoundError): 
        print("Arquivo Excel não encontrado")
        return None

def read_template(template_path):
    if exists(template_path):
        return DocxTemplate(template_path)
    print("Arquivo Template Docx não encontrado")
    return None

activities_table = read_table(argv[1])
template = read_template(argv[2])

all_activities = activities_table[["Data", "Atividades", "Horas"]]
brute_weekly_data = dict(all_activities)
weekly_data = {}

# weeks
for i in range(5):
    weekly_data[f'week{i}'] = []
    # days
    for j in range(5):
        if ((i * 5 + j) >= len(all_activities.index)):
            break

        dia = brute_weekly_data['Data'][i * 5 + j]
        if pd.isnull(dia) or dia == '-':
            dia = "-"
        else:
            dia = dia.strftime("%d/%m")

        hora = brute_weekly_data['Horas'][i * 5 + j]
        if pd.isnull(hora) or hora == '-':
            hora = "-"
        else:
            hora = hora.strftime("%H:%M")

        activity = brute_weekly_data['Atividades'][i * 5 + j]

        if (activity != '-'):
            weekly_data[f'week{i}'].append({
                'date': dia, 'activity': brute_weekly_data['Atividades'][i * 5 + j],
                'hours': hora
            })

hours_sum = []
for i in range(5):
    hours_sum.append(activities_table.iloc[6 + i, 5].strftime("%H:%M"))

total_sum = activities_table.iloc[3, 4]
total_sum = f"{total_sum.hour + total_sum.day * 24}:{total_sum.minute if total_sum.minute != 0 else '00'}"

today = date.today()
months = {
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

template.render({'weekly_data': weekly_data,
    'hours_sum': hours_sum,
    'total_sum': total_sum,
    'month': months[str(today.month)],
    'year': today.year,
    'scholarship_number': today.month - 2})
template.save(argv[3])
