import json
from datetime import datetime

# записываем в data (словарь) данные из файла формата json с помощью специальной функции
# ставим кодировку, чтобы пропечаталась кириллица
with open('json_test1.json', encoding = 'utf-8') as f_input:
    data = json.load(f_input)

# дата, которая задана в задании
check_date = datetime(2021, 9, 1)

# проходимся по списку из словарей, специальными преобразованиями делаем сравнение и удаляем ненужные события
for i, element in enumerate(data['data']):
    if (abs((datetime.strptime(element['date'], '%Y-%m-%d') - check_date).days) > 10):
        del data['data'][i]

# выводим ответ в отдельный файл с помощью специальной функции
with open('answer.json', 'w') as f_output:
    json.dump(data, f_output, ensure_ascii = False)
