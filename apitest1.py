import requests
import json

#api server ip:port
url = 'http://localhost:5000'
#get voltage
req_dict1 = {
    'ActionType': 'get_voltage',
}


#1
ret_dict = requests.post(url=url, json=req_dict1)
print(ret_dict.json())
