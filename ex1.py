import json
from datetime import datetime, timedelta


def StrToData(s):
    return datetime.strptime(s, '%Y-%m-%d')


def AddData(json, text, date):
    return json['data'].append({'text' : text, 'date' : date})


jsonData = {
    "user_id": 123,
    "data": [
        {
            "text": "Событие №1",
            "date": "2021-05-30"
        },
        {
            "text": "Событие №2",
            "date": "2021-08-31"
        },
        {
            "text": "Событие №3",
            "date": "2021-09-12"
        }
    ]
}

controlData = StrToData('2021-09-01')
daysCount = 10
minDate = controlData - timedelta(days=daysCount)
maxDate = controlData + timedelta(days=daysCount)


newJson = {}
newJson['user_id'] = jsonData.get('user_id')
newJson['data'] = []


for el in jsonData['data']:
    thisDate = StrToData(el.get('date'))
    if(thisDate > minDate and thisDate < maxDate):
        AddData(newJson, el.get('text'), el.get('date'))


with open('rezult.json', 'w') as outfile:
    json.dump(newJson, outfile, ensure_ascii = False)
