
# 다른 애들 끝나면 다시 시도.


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time


# 쿼리문 https://talosintelligence.com/reputation_center/lookup?search=4.2.2.1

try:
    ip="121.53.105.193"
    url = f"https://talosintelligence.com/reputation_center/lookup?search={ip}"

    chrome_options = Options() 
    chrome_options.add_experimental_option("detach", True) 
    driver = webdriver.Chrome(options=chrome_options) 
    time.sleep(10)
    driver.get(url)
except:
    print("nope")
while True:
    pass

        



