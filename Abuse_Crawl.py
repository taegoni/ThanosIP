# Abuse_Crawl.py
# API 결과값 받아오기 성공

import requests
import json
from variableFile import AbuseAPI

# ip list 파일 열고 output 저장할 변수 선언
ip_file = open("laBel_sample0001.txt", 'r')
ip_output = open("ip_output.txt", 'a')

# 16째 줄부터 (ip 부분만) 읽기
ip_line = ip_file.readlines()[15:]

# ip 뒤에 줄바꿈 문자 제거
i = 0
only_ip = []
while i < len(ip_line) :
    only_ip.append(ip_line[i].rstrip("\n"))
    i += 1

print(only_ip)

# for문으로 ip 한줄씩 반복 검색하기
i = 0
while i < len(only_ip) :

    # Defining the api-endpoint
    url = 'https://api.abuseipdb.com/api/v2/check'

    querystring = {
        
        'ipAddress': only_ip[i],
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': AbuseAPI
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    # Formatted output
    decodedResponse = json.loads(response.text)
    # print(json.dumps(decodedResponse, sort_keys=True, indent=4))
    ip_output.write(json.dumps(decodedResponse, sort_keys=True, indent=4)) # output 파일에 쓰기

    i += 1

# ip list 파일 닫기
ip_file.close()
ip_output.close()