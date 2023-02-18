import json
import openpyxl

woorkbook = openpyxl.load_workbook("backend/Маппинг сигналов.xlsx")

# 1) мапа для соответствия сигнала с кафки

signals_mapping = {}
reading_warnings = False
kafka_signal = None
current_part = None

for sheet in woorkbook.sheetnames:
    worksheet = woorkbook[sheet]
    for row in list(worksheet.values)[1:]:
        if row[0] is not None:
            current_part = row[0]
            current_parameter = row[1]
            reading_warnings = False
            kafka_signal = row[4]
        if row[1] is not None:
            current_parameter = row[1]
            reading_warnings = False
            kafka_signal = row[4]
        if row[2] is not None:
            if row[2] == 'Уставки':
                reading_warnings = True
            else:
                kafka_signal = row[4]
                reading_warnings = False
                parameter_type = row[2]
        if row[0] is None and row[1] is None and row[2] is None and not reading_warnings:
            kafka_signal = row[4]
        if reading_warnings:
            signals_mapping[kafka_signal]['has_warnings'] = True
            signals_mapping[kafka_signal][row[3]] = row[4]
        else:
            signals_mapping[kafka_signal] = {
                'name': row[5],
                'current_part': current_part,
                'parameter_name': row[1],
                'parameter_type': row[2],
                'parameter_enum': row[3],
                'number': sheet,
                'has_warnings': False
            }

with open('backend/mapping.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(signals_mapping, ensure_ascii=False))
