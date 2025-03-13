from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options=Options()

options.add_argument("--start-maximized")
## 화면 안꺼짐 이거있으면

options.add_experimental_option("detach",True)

service=Service(ChromeDriverManager().install())

driver=webdriver.Chrome(service=service,options=options)

url="https://naver.com"
driver.get(url)
time.sleep(2)