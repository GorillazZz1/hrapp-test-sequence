# hrapp-test-sequence
Task 2  
```{python}< >{
import json  
from datetime import datetime  
import numpy as np  
def relevant_events(jsonstr):  
    pydict = json.loads(jsonstr)   
    for item in pydict['data']:  
        item['date'] = datetime.strptime(item['date'], '%Y-%m-%d').date()  
        if abs((item['date'] - date(2021, 9, 1)).days) > 10:  
               pydict['data'].remove(item)  
    print(json.dumps(pydict, ensure_ascii=False, indent=4))
		
```
		
Task 3
```{python}< >{
from jinja2 import Template
def agrdata(main_data):
    for item in main_data["data"]:
        if float(item["sum"].replace(',', '.').replace(' ', '')) > 100:
            print(Template("{{ item['name'] }} - {{ item['sum'] }}").render(item = item))
```

Task 4
```{python}< >{
import json
from jinja2 import Template
pydict = {
        "app_hello": {
            "type": "base",
            "actions": [
                {
                    "type": "sdk_answer_to_user",
                    "static": {
                        "ios_card": {
                            "type": "list_card",
                            "cells": [
                                {
                                    "ios_params": "ios"
                                }
                            ]
                        },
                        "android_card": {
                            "type": "list_card",
                            "cells": [
                                {
                                    "android_params": "android"
                                }
                            ]
                        },
                        "static_sg_dl": "www.www.www",
                        "static_sg_text": "static suggest text"
                    },
                    "random_choice": [
                        {
                            "random_choice_greeting": "Good morning!"
                        },
                        {
                            "random_choice_greeting": "Good afternoon!"
                        },
                        {
                           "random_choice_greeting": "Good evening!" 
                        }
                    ],
                    "root":
                        [
                            {
                                "type": "pronounce_text",
                                "text": "random_choice_greeting"
                            }
                        ],
                    "items": [
                        {
                            "type": "item_card",
                            "text": "ios_card",
                            "requirement": {
                                "type": "external",
                                "requirement": "OCTOBER_iOS"
                            }
                        },
                        {
                            "type": "item_card",
                            "text": "android_card",
                            "requirement": {
                                "type": "external",
                                "requirement": "OCTOBER_android"
                            }
                        },
                        {
                            "type": "bubble_text",
                            "text": "random_choice_greeting"
                        }
                    ]
    }
            ]
        }
    }
scenario = json.dumps(pydict, ensure_ascii=False, indent=4) 
print(scenario)
```
