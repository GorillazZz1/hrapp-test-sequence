from jinja2 import Template
import json

sample = """{
    "data": [
        {
            "name": "Саша",
            "sum": "42,50"
        },
        {
            "name": "Оля",
            "sum": "100,50"
        },
        {
            "name": "Сережа",
            "sum": "10 000,00"
        }
    ]
}"""
data = json.loads(sample)

with open('task3.j2') as f:
    temp = Template(f.read(), trim_blocks=True)

print(temp.render(data=data), end='')