import json
import requests
file_path="./teniron.json"
with open(file_path,'r',encoding='utf-8') as file:
        data =json.load(file)
        url,private_key = data["Ailabs"].values()
ip="222.99.77.39"
query=url
x = requests.get(query)
# print(x)
print(json.loads(x.text))

