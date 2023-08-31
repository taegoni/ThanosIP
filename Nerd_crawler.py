import json
import requests
file_path="./teniron.json"
with open(file_path,'r',encoding='utf-8') as file:
        data =json.load(file)
        url,private_key = data["Nerd"].values()
ip="222.99.77.39"
query=f'{url}/ip/{ip}/rep'
x = requests.get(query,headers={"Authorization":f'token {private_key}'})
print(x)
print(json.loads(x.text))
