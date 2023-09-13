import requests
import json
import apikey

file = open("laBel_sample0001.txt",'r')

line = file.readlines()

criminalip_summary = open('criminalip_summary.txt','w')
try :
  for i in line :
    i = i.strip()
    if '#' not in i :
      url = "https://api.criminalip.io/v1/feature/ip/privacy-threat?ip={}".format(i)

      payload={}
      headers = {
        "x-api-key": "{}".format(apikey.criminalip_apikey)
      }

      response = requests.request("GET", url, headers=headers, data=payload)
      data = response.json()

      formatted_data = json.dumps(data, indent=3)
      criminalip_summary.write(formatted_data)
except :
  print("Error")
criminalip_summary.close()
file.close()