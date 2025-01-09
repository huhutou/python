import random
import requests
import json
url="http://10.180.12.54:7001/uac_oa/getSalt"
data={
    "csrftoken":""
}
params={
    "r":0.669808750856898
}
salt=requests.post(url,params=params,data=data)
print(salt.json())