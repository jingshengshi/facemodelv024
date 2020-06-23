import requests
import json

#api server ip:port
url = 'http://localhost:5000'
 
#speed
req_dict3 = {
    'ActionType': 'blink',
    'ActionParams':{
        'action': "speed",
        'speed': 50
    }
}


#3
ret_dict = requests.post(url=url, json=req_dict3)
print(ret_dict.json())
