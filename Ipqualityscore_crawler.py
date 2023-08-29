import json
import requests
file_path="./teniron.json"
with open(file_path,'r',encoding='utf-8') as file:
        data =json.load(file)
        url,private_key = data["Ipqualityscore"].values()
ip="222.99.77.39"
strictness="0"
allow_public_access_points="true"
fast="true"
lighter_penalties="true"
mobile="true"
option = "&".join([f'strictness={strictness}',f'allow_public_access_points={allow_public_access_points}',
                   f'fast={fast}',f'lighter_penalties={lighter_penalties}',f'mobile={mobile}'])
query=url+private_key+'/'+ip+"?"+option
x = requests.get(query)
print(200)
print(json.loads(x.text))

