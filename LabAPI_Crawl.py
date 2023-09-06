import requests
import json
from tqdm import tqdm

url = ('https://github.com/monitorapp-aicc/feed/blob/main/ip.txt')

t = 0
for t in tqdm(range(1), desc='Processing'):
    response = requests.request(method='GET', url=url)

    # Formatted output
    decodedResponse = json.loads(response.text)
    #print(json.dumps(decodedResponse, sort_keys=True, indent=4))

    print(decodedResponse)

