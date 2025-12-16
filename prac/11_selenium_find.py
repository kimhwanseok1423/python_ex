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


"""
<input id="query" name="query" type="search" title="검색어를 입력해 주세요.
 " placeholder="검색어를 입력해 주세요." maxlength="255"
  autocomplete="off" class="search_input" data-atcmp-element="">

"""
driver.find_element(By.XPATH,'//*[@title="검색어를 입력해 주세요."]').send_keys("블랙핑크",Keys.ENTER)
time.sleep(2)
# driver.find_element(By.XPATH, '//*[text()="블로그"]').click()


# 텍스트가 링크인 블로그를 찾을떄 씀
driver.find_element(By.LINK_TEXT,"블로그").click()
time.sleep(2)
# 정확히 안써도 찾아줌 PARTIAL_LINK_TEXT
driver.find_element(By.PARTIAL_LINK_TEXT,"인플루언").click()
