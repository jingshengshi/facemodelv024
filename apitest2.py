import requests
import json

#api server ip:port
url = 'http://localhost:5000'


req_dict2 = {
    'ActionType': 'blink',
    'ActionParams':{
        'action': "run",
        'times' : 1
    }
}

#2
ret_dict = requests.post(url=url, json=req_dict2)
print(ret_dict.json())
