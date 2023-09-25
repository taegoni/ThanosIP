from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# subprocess.Popen(r'C:/Program Files/Google/Chrome/Application/chrome.exe --remote-debugging-port=9222 --user-data-dir="./chrometemp"')

try:
    ip="121.53.105.193"
    url = f"https://talosintelligence.com/reputation_center/lookup?search={ip}"
    # url="https://www.naver.com"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
except:
    print("nope")
