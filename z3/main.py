from os import replace
import jinja2
import sys
import json

if __name__ == '__main__':   
    # Если название json-файла указано через аргументы командной строки 
    if len(sys.argv) == 2:      
        filename = sys.argv[1] 
        # Считыание json из файла
        with open(filename, 'r', encoding = 'utf-8') as j:
            json_data = json.load(j)               
    else:
        x = input("Введите строку в формате json: ")
        json_data = json.loads(x)      

    # Определяем класс загрузчика шаблонов из файловой системы
    # (`temp` - папка где лежит сохраненный шаблон 'temp.txt')
    loader = jinja2.FileSystemLoader('temp')
    # Определяем переменную среду, в которую передаем загрузчик
    env = jinja2.Environment(loader=loader, trim_blocks = True)

    # функции для обработки строки
    json_data['float'] = float
    json_data['replace'] = replace
    
    # загружаем шаблон 'temp.txt'
    tpl = env.get_template('temp.txt')
    # рендерим шаблон в переменную `result`
    result = tpl.render(json_data)

    # Сохраним получившийся текст
    with open('result.txt', 'w', encoding = 'utf-8') as fp: 
        fp.write(result)

    # Прочитаем записанный файл
    with open('result.txt', 'r', encoding = 'utf-8') as fp: 
        print(fp.read())
