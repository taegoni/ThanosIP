import requests
import json

file = open("laBel_sample0001.txt",'r')

line = file.readlines()

criminalip_malicious_info = open('criminalip_malicious_info.txt','w')

try :
        
    for i in line :
        if '#' not in i :
            url = "https://api.criminalip.io/v1/feature/ip/malicious-info?ip={}".format(i)

            payload = {}
            headers = {
                "x-api-key": "tnlZ7BUgf7GjqOBlbCA68i5ZF7J30q2Rn2NDygbkX1m87RzCl0x6u4R41hYL"
            }

            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()

            formatted_data = json.dumps(data, indent=3)
            criminalip_malicious_info.write(formatted_data)
except :
    print("Error")
criminalip_malicious_info.close()
file.close()    