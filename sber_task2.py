from jinja2 import Template

main_data = {
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
}

ans = '''{% for item in main_data.data %} 
{%- if item.sum.replace(',', '.').replace(' ', '')|float > 100 -%}  
{{item.name}} - {{item.sum}} 
{% endif -%} 
{% endfor %}'''

template = Template(ans)

print(template.render(main_data = main_data))



