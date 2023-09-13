import requests
import json
import sys



url = "https://api.criminalip.io/v1/feature/ip/malicious-info?ip=31.43.185.32"

payload = {}
headers = {
    "x-api-key": "tnlZ7BUgf7GjqOBlbCA68i5ZF7J30q2Rn2NDygbkX1m87RzCl0x6u4R41hYL"
}

response = requests.get(url, headers=headers, data=payload)
data = response.json()

formatted_data = json.dumps(data, indent=3)
print(formatted_data)

