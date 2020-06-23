import requests
import json

#api server ip:port
url = 'http://localhost:5000'

#loop
req_dict4 = {
    'ActionType': 'blink',
    'ActionParams':{
        'action': "run",
        'times' : 0
    }
}

#4
ret_dict = requests.post(url=url, json=req_dict4)
print(ret_dict.json())
