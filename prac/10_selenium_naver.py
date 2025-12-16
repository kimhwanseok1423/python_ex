from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

driver.find_element(By.ID,"query").send_keys("뉴진스")
time.sleep(2)

# css+selector > id면 # class는 기본
driver.find_element(By.CSS_SELECTOR,"#search-btn").click()
time.sleep(2)

# 검색후 class 값에서 0 , 1 , 2번째 껄 클릭할때 씀
# driver.find_elements(By.CLASS_NAME, "flick_bx")[2].click()

# 검색마다 2번쨰것이 블로그 탭이 아닐수있으므로 XPATH 사용
# driver.find_element(By.XPATH, '//*[text()="블로그"]').click()

driver.find_elements(By.XPATH,'//*[text()="블로그"]')[2].click()
time.sleep(2)

driver.find_element(By.NAME,"query").clear()
time.sleep(2)

driver.find_element(By.NAME,"query").send_keys("에스파")
time.sleep(2)


driver.find_element(By.NAME,"query").send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element(By.TAG_NAME,"body").send_keys(Keys.END)
time.sleep(2)


driver.save_screenshot("selenium_naver/naver.png")
print("스크린샷을 저장했습니다.")

driver.quit()