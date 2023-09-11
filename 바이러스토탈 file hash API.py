import requests

v_url = 'https://www.virustotal.com/vtapi/v2/file/report'
params = {'apikey' : 'f50fe40dd128c111a0def3c9c1276c804d1ec03ee8f261b062de8540ff39b915' , 'resource' : '31697d421c4b1995cdf0a2fa0bf6fe6d'}

response = requests.get(v_url, params=params)

result = response.json()

det= 0

# print(result)

for x in result['scans'] :
    if result['scans'][x]['detected'] :
        det = det + 1
        print("{0:22} : {1}".format(x,result['scans'][x]['result']))
    
print("{0} engines detected this file".format(det))