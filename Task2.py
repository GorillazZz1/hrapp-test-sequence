import json
from datetime import datetime
date = datetime.strptime('01.09.2021', '%d.%m.%Y')
with open('input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, event in enumerate(data['data']):
    curr = datetime.strptime(event['date'], '%Y-%m-%d')
    if abs((curr - date).days) > 10:
        del data['data'][i]
with open('output.json', 'w', encoding='utf-8') as out:
    json.dump(data, out)