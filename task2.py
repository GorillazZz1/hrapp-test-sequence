from datetime import datetime as dt
import json

sample = """{
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
"""


def show_dates(sample):
    # sample - строка в формате json
    data = json.loads(sample, encoding="utf-8")

    data['data'] = [event for event in data['data'] if abs(
        (dt.strptime(event['date'], '%Y-%m-%d')-dt(2021, 9, 1)).days) <= 10]

    return json.dumps(data, indent=3, ensure_ascii=False)


print(show_dates(sample))
