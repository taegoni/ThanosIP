from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
try:
    ip="121.53.105.193"
    url = f"https://www.barracudacentral.org/lookups/lookup-reputation"
    chrome_options = Options() 
    chrome_options.add_experimental_option("detach", True) 
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.find_element(By.CSS_SELECTOR,"#ir_entry").send_keys(ip)
    driver.find_element(By.CSS_SELECTOR,'#lookup-reputation > div > div.yui-u.first > form > fieldset > div:nth-child(3) > input[type=submit]:nth-child(2)').click()   
    time.sleep(1)

    print(driver.find_element(By.CSS_SELECTOR,"#lookup-reputation > div > div.yui-u.first > form > fieldset > p").text)

except:
    print("err0r err0r err0r err0r err0r err0r err0r")
while True:
    pass

        



