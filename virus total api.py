import requests

url = "https://www.virustotal.com/api/v3/ip_addresses/31.43.185.32"

headers = {"accept": "application/json", "x-apikey" :"f50fe40dd128c111a0def3c9c1276c804d1ec03ee8f261b062de8540ff39b915" }

response = requests.get(url, headers=headers)

result = response.json()

print(response.text)

# for i in result['data']['attributes']['last_analysis_results'] :
#     print("{:<30} : {}".format(i,result['data']['attributes']['last_analysis_results'][i]['category']))
      

    