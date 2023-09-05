from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time
from tqdm import tqdm

def Selenium_crawl(i,u):
    chrome_options = Options() 
    chrome_options.add_experimental_option("detach", True) 
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(u)
    driver.find_element(By.CSS_SELECTOR,"#ir_entry").send_keys(i)
    driver.find_element(By.CSS_SELECTOR,'#lookup-reputation > div > div.yui-u.first > form > fieldset > div:nth-child(3) > input[type=submit]:nth-child(2)').click()
    # 봇으로 인식되지 않도록?
    time.sleep(0.5)
    return new.write(driver.find_element(By.CSS_SELECTOR,"#lookup-reputation > div > div.yui-u.first > form > fieldset > p").text + "\n")
    
     
     

file_path="./teniron.json"
with open(file_path,'r',encoding='utf-8') as file:
    data = json.load(file)
    url,private_key = data["BarracudaCentral"].values()

ip_list_path="laBel_sample0001.txt"
new = open(f'barracuda_result_{ip_list_path}','w')
retry_list=[]
with open(ip_list_path,'r',encoding='utf-8') as ips:
        for line in tqdm(ips.readlines(),desc='1차 크롤링'):
            try:
                if line[0]=="#":
                        continue
                else:
                    ip=line.strip()
                    Selenium_crawl(ip,url)
            except:
                retry_list.append(ip)
        pending=[]
        for ret in tqdm(range(len(retry_list)),desc="재시도 1차"):
            try:
                ip=retry_list[ret]
                Selenium_crawl(ip,url)
            except:
                 pending.append(ip)

new.write(f"not working : {pending}"+"\n")
                     
new.close()