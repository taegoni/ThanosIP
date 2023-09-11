import requests
import json
import sys
import winsound as sd
from tqdm import tqdm

file = open("laBel_sample0001.txt",'r')

line = file.readlines()

criminalip_data = open('criminalip_data.txt','w')


try :
  for i in tqdm((line),desc="progress") : 
    if '#' not in i :
      url = "https://api.criminalip.io/v1/ip/data?ip={}".format(i)
      payload={}
      headers = {
        "x-api-key": "tnlZ7BUgf7GjqOBlbCA68i5ZF7J30q2Rn2NDygbkX1m87RzCl0x6u4R41hYL"
      }

      response = requests.request("GET", url, headers=headers, data=payload)
      data = response.json()

      formatted_data = json.dumps(data, indent=3)
      criminalip_data.write(formatted_data)
except :
  print("Error")

criminalip_data.close()
file.close()

#비프음
def beepsound() :
    fr = 2000
    du = 1000
    sd.Beep(fr,du)
beepsound()
