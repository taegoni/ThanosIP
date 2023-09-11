import requests
import json
import sys

file = open("laBel_sample0001.txt",'r')

line = file.readlines()

criminalip_summary = open('criminalip_summary.txt','w')
try :
  for i in line :
    if '#' not in i :
      url = "https://api.criminalip.io/v1/ip/vpn?ip={}".format(i)

      payload={}
      headers = {
        "x-api-key": "tnlZ7BUgf7GjqOBlbCA68i5ZF7J30q2Rn2NDygbkX1m87RzCl0x6u4R41hYL"
      }

      response = requests.request("GET", url, headers=headers, data=payload)
      data = response.json()

      formatted_data = json.dumps(data, indent=3)
      criminalip_summary.write(formatted_data)
except :
  print("Error")
criminalip_summary.close()
file.close()