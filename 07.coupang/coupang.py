from selenium import webdriver
from bs4 import BeautifulSoup
import time


# WebDriver 실행
#service = Service(ChromeDriverManager().install())

url="http://naver.com"
driver = webdriver.Chrome()

driver.get(url)
html=driver.page_source
time.sleep(3)

# title=driver.title

# print(title)

soup=BeautifulSoup(html,"html.parser")

logo=soup.select_one(".service_name").text
print(logo)
