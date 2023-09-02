import json
import requests
import time
file_path="./teniron.json"
with open(file_path,'r',encoding='utf-8') as file:
        data =json.load(file)
        url,private_key = data["Nerd"].values()

ip_list_path="./banlist.txt"
# ip="222.99.77.39"
new = open('NERD_result.txt','w')
with open(ip_list_path,'r',encoding='utf-8') as ips:
        for line in ips.readlines():
                if line[0]=="#":
                        continue
                else:               
                        ip = line
                        query=f'{url}/ip/{ip}/full'
                        x = requests.get(query,headers={"Authorization":f'token {private_key}'})
                        # print(x)
                        # print(json.loads(x.text))
                        new.write(x.text+"\n")

# ! TODO: \n 처리, 에러시 ip들만 따로 모아두기. 마지막이나 맨앞에 기록하도록.

new.close()
        

