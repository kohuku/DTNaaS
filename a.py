

import requests

addr = "http://74.114.96.105:5000/create_file/"

data = {
            'hello_world' : {                
                'size' : '100M'
            },
            'hello_world2' : {
                'size' : '100M'
            }
        }  
response = requests.post(addr,data=data)
print(response)



