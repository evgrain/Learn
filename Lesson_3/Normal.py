# coding: utf-8
import io


names = ['Игорь', 'Олег', 'Денис', 'Ирина', 'Пётр']
payment = ['65000', '45000', '500000', '51000', '90000']
data_from_file = []
data_to_file = (dict(zip(names, payment)))
file_out = open('salary.txt', 'w', encoding='utf-8')
for key in data_to_file:
    line = key + ' - ' + data_to_file[key] + '\n'
    file_out.write(line)
file_out.close()
with io.open('salary.txt', encoding='utf-8') as file:
    for line in file:
        data_from_file.append(line.strip())
for line in data_from_file:
    format_data = line.split(' - ')
    for value in format_data:
        if int(format_data[1]) < 500000:
            map(lambda x: x.upper(), format_data)
            print(value.upper(), '-', (lambda x: round(int(x) - (int(x) *0.13)))(format_data[1]))
            break
