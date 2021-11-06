import sys
import json
from datetime import datetime, timedelta

# дата, относительно которой будет проверка
CHECK_DATE = '01.09.2021'
# формат записи даты, относительно которой проверка
FORMAT_DATE_1 = '%Y-%m-%d'
# формат запсии даты из json-строки
FORMAT_DATE_2 = '%d.%m.%Y'
# кол-во дней, которые определяют временной промежуток
NUM_DAYS = 10

def check_json(data):
    res = dict()
    res['data'] = []

    date = datetime.strptime(CHECK_DATE, FORMAT_DATE_2)
    # верхняя граница искомого временного промежутка
    date_up = date + timedelta(NUM_DAYS)
    # нижняя граница искомого временного промежутка 
    date_low = date - timedelta(NUM_DAYS)

    for key in data:
        val = data[key]
        if (type(val) == list):
            for item in val:
                # преобразование даты в строке в формат datetime (формат записи даты - format_1)
                date_cur = datetime.strptime(item['date'], FORMAT_DATE_1)
                # если дата входит в заданный промежуток, то добавляем событие в результат
                if (date_low <= date_cur <= date_up):
                    res['data'].append(item)
        else:
            res[key] = val

    return json.dumps(res, ensure_ascii=False)


if __name__ == '__main__':   
    # Если название json-файла указано через аргументы командной строки 
    if len(sys.argv) == 2:      
        filename = sys.argv[1] 
        # Считыание json из файла
        with open(filename, 'r', encoding='utf-8') as j:
            json_data = json.load(j)        
            res = check_json(json_data)        
    else:
        x = input("Введите строку в формате json: ")
        json_data = json.loads(x)      
        res = check_json(json_data)
    print(res)