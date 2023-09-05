import json
import requests
from tqdm import tqdm

file_path="./teniron.json"
with open(file_path,'r',encoding='utf-8') as file:
        data =json.load(file)
        url,private_key = data["Nerd"].values()

ip_list_path="laBel_sample0001.txt"
# ip_list_path="banlist.txt"

# 옵션에 따라 full rep fmt 등등으로 나눠볼 예정.            
option=["full","rep","fmt"]
clean_list=[]
retry_list=[]
new = open(f'NERD_result_{ip_list_path}','w')
with open(ip_list_path,'r',encoding='utf-8') as ips:
        for line in tqdm(ips.readlines(),desc='1차 크롤링'):
                if line[0]=="#":
                        continue
                else:   
                        ip = line.strip()
                        query=f'{url}/ip/{ip}/{option[0]}'
                        res_raw = requests.get(query,headers={"Authorization":f'token {private_key}'})
                        res_json = json.loads(res_raw.text)
                        if res_json.get("err_n"):
                                if res_json["err_n"]>=500:
                                        retry_list.append(ip)
                                elif res_json["err_n"]>=400:
                                        clean_list.append(ip)
                        else:
                                new.write(res_raw.text+"\n")
        pending=[]
        for ret in tqdm(range(len(retry_list)),desc="재시도 1차"):
                ip=retry_list[ret]
                res_raw = requests.get(query,headers={"Authorization":f'token {private_key}'})
                res_json = json.loads(res_raw.text)
                if res_json.get("err_n")>=500:
                        pending.append(ip)
                elif res_json.get("err_n")>=400:
                        clean_list.append(ip)
                else:
                        new.write(res_raw.text+"\n")
        
        new.write(f'"clean_list":{clean_list}'+"\n")
        new.write(f"http 500+ : {pending}"+"\n")


new.close()