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

main_template = Template('''
{%- for el in main_data.data -%}
{%- set sum = el.sum.replace(',','.').replace(' ','')|float -%}
{%- if sum > 100 -%}
{{ el.name }} - {{ el.sum }}
{% endif %}
{%- endfor -%}
''')


print(main_template.render(main_data = main_data))