import requests

ip = '31.43.185.32'

url = "https://www.virustotal.com/api/v3/ip_addresses/{ip}"



headers = {"accept": "application/json", "x-apikey" :"f50fe40dd128c111a0def3c9c1276c804d1ec03ee8f261b062de8540ff39b915"}

response = requests.get(url, headers=headers)

print(response.text)