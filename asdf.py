import requests
import json

url = "https://api.criminalip.io/v1/feature/ip/malicious-info?ip=185.156.46.101"

payload={}
headers = {
  "x-api-key": "tnlZ7BUgf7GjqOBlbCA68i5ZF7J30q2Rn2NDygbkX1m87RzCl0x6u4R41hYL>"
}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()

formatted_data = json.dumps(data, indent=3)

print(formatted_data)