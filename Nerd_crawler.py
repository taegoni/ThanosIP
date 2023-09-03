
# ! 우선 사항 -> 메뉴 형식으로 기능을 정의하여 다양한 API를 사용할 수 있도록 하기.
# ! 개발 레벨 정하기? 1단계 기능 완성 2단계 모듈화 3단계 코드 효율성 증대.
# ! TODO: 에러시 ip들만 따로 모아 저장. 마지막이나 맨앞에 기록하도록 하기.
# 진행도 표기하기..
# ? DB에서 이미 존재하는지 확인하는 기능은 어떻게 구현할 것인지.. 순서의 문제..

import json
import requests

file_path="./teniron.json"
with open(file_path,'r',encoding='utf-8') as file:
        data =json.load(file)
        url,private_key = data["Nerd"].values()

ip_list_path="./banlist.txt"
# ip="222.99.77.39"
option=["full","rep","fmt"]
clean_list=[]
retry_list=[]
new = open('NERD_result2.txt','w')
with open(ip_list_path,'r',encoding='utf-8') as ips:
        for line in ips.readlines():
                if line[0]=="#":
                        continue
                else:   
                        # 옵션에 따라 full rep fmt 등등으로 나눠볼 예정.            
                        ip = line.strip()
                        query=f'{url}/ip/{ip}/{option[0]}'
                        res_raw = requests.get(query,headers={"Authorization":f'token {private_key}'})
                        res_json = json.loads(res_raw.text)
                        # server error
                                # 방법 1. 바로 재시도
                                # 1. 서버 에러이므로 5초 후 재시도, 3회 재시도 후 안되면 종료, 재시도 시 로그 남기기.
                                # 2. 저장이 필요한 데이터 : err_n, error, ip. => 로그에 저장
                                
                                # ! 방법 2. 모아서 나중에 재시도 (특정 사이트에 적용)
                                # 1. 에러 발생시 ip만 그냥 모아둠.
                                # 2. 끝까지 진행후 다시 재시도(sleep 1)

                        if res_json.get("err_n"):
                                if res_json["err_n"]>=500:
                                        retry_list.append(ip)
                                elif res_json["err_n"]>=400:
                                        clean_list.append(ip)
                        else:
                                new.write(res_raw.text+"\n")
        last=[]
        for ret in range(len(retry_list)):
                ip=retry_list[ret]
                res_raw = requests.get(query,headers={"Authorization":f'token {private_key}'})
                res_json = json.loads(res_raw.text)
                if res_json.get("err_n")>=500:
                        last.append(ip)
                elif res_json.get("err_n")>=400:
                        clean_list.append(ip)
                else:
                        new.write(res_raw.text+"\n")
        
        if last:
                new.write(f'"client error":{last}')


new.close()
        

