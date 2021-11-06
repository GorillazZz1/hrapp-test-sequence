import json
import datetime

def my_func(json_string, main_date = datetime.datetime(2021, 9, 1), delta_days = 10):
	arr = json.loads(json_string) #Creating dict from json_string
	
	i = 0
	while(i < len(arr['data'])):
		date = datetime.datetime.strptime(arr['data'][i]['date'], "%Y-%m-%d") #Creating datetime object
		delta = date - main_date 
		if(abs(delta.days) >= delta_days): #Removing element if difference is larger than delta_days
			arr['data'].pop(i)
			i -= 1 #Counter must remain constant if element had been popped
		i += 1
	return(json.dumps(arr))
