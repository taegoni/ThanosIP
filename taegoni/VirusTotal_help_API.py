import requests
import apikey

v_url = 'https://www.virustotal.com/vtapi/v2/file/report'
params = {'apikey' : '{}'.format(apikey.virustotal_apikey) , 'resource' : '31697d421c4b1995cdf0a2fa0bf6fe6d'}

response = requests.get(v_url, params=params)

result = response.json()

det= 0

# print(result)

for x in result['scans'] :
    if result['scans'][x]['detected'] :
        det = det + 1
        print("{0:22} : {1}".format(x,result['scans'][x]['result']))
    
print("{0} engines detected this file".format(det))

# for i in result['data']['attributes']['last_analysis_results'] :
#     print("{:<30} : {}".format(i,result['data']['attributes']['last_analysis_results'][i]['category']))
      
