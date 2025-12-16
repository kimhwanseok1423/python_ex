from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


options=Options()

options.add_argument("--start-maximized")

options.add_experimental_option("detach",True)

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=options)

url="https://naver.com"

driver.get(url)
time.sleep(2)


navs=driver.find_elements(By.CLASS_NAME,"link_service")

# print(navs)
# # print()
# # print(dir(navs[0]))
# # print()
# # print(len(navs))


for num,nav in enumerate(navs,1):
    # print(num)
    # #link_service를 가지고있는 html을 출력함
    # print(nav.get_attribute("outerHTML"))
    # print(nav.text)
    # print()
    if nav.text =="웹툰":
        nav.click()
        break
time.sleep(2)

driver.quit()