import requests
import json

url = ('https://github.com/monitorapp-aicc/feed/blob/main/ip.txt')

response = requests.request(method='GET', url=url)

# Formatted output
decodedResponse = json.loads(response.text)
print(json.dumps(decodedResponse, sort_keys=True, indent=4))