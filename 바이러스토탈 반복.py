import requests
import sys
import winsound as sd
from tqdm import tqdm


file = open("laBel_sample0001.txt",'r')

line = file.readlines()

sys.VirusTatal = open('VirusTatal.txt','w')


try :  
    for i in tqdm((line),desc="progress") : 
        if '#' not in i :
            url = "https://www.virustotal.com/api/v3/ip_addresses/{}".format(i)
            headers = {"accept": "application/json", "x-apikey" : "f50fe40dd128c111a0def3c9c1276c804d1ec03ee8f261b062de8540ff39b915"}
            response = requests.get(url, headers=headers)
            result = response.json()

            if result['data']['attributes']['last_analysis_stats']['harmless'] > 0 and result['data']['attributes']['last_analysis_stats']['malicious'] == 0 :
                sys.VirusTatal.write('\"harmless\" : {} '.format(response.text))
               
            elif result['data']['attributes']['last_analysis_stats']['malicious'] > 0 :
                sys.VirusTatal.write('\"malicious\" : {} '.format(response.text))

            elif result['data']['attributes']['last_analysis_stats']['undetected'] == result['data']['attributes']['last_analysis_stats']['harmless'] + result['data']['attributes']['last_analysis_stats']['malicious'] + result['data']['attributes']['last_analysis_stats']['suspicious'] + result['data']['attributes']['last_analysis_stats']['undetected'] :
                sys.VirusTatal.write('\"undetected\" : {} '.format(response.text))
except :
    print("Error")
sys.VirusTatal.close()

file.close()

#비프음
def beepsound() :
    fr = 2000
    du = 1000
    sd.Beep(fr,du)
beepsound()
