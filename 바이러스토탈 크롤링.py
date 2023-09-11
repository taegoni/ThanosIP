import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("<<<ip를 검색하세요>>>")
response = requests.get(f"https://www.virustotal.com/gui/ip-address/{keyword}")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
#links = soup.select("//*[@id="report"]/vt-ui-ip-card//div/div[1]/div[1]")
information_list = soup.css.select_one("div")
print(information_list)
# for information in information_list:
# 	print(information.text)
        
# for link in links :
#     title = link.text
#     print(title)

