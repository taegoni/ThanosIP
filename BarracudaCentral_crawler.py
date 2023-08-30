from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
try:
    ip="121.53.105.193"
    url = f"https://www.barracudacentral.org/lookups/lookup-reputation"
    chrome_options = Options() 
    chrome_options.add_experimental_option("detach", True) 
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.find_element(by='ir_entry').send_keys(ip)
    driver.find_element(by='lookup-reputation').click()   
        
except:
    print("nope")
while True:
    pass

        



