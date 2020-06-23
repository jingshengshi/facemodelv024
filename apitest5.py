import requests
import json

#api server ip:port
url = 'http://localhost:5000'
#stop
req_dict5 = {
    'ActionType': 'stop',
}


#1
ret_dict = requests.post(url=url, json=req_dict5)
print(ret_dict.json())
