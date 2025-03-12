# 필요한 패키지를 설치합니다.
# pip install selenium webdriver-manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriverManager를 통해 ChromeDriver를 자동으로 설치하고, 경로를 설정합니다.
driver = webdriver.Chrome(ChromeDriverManager().install())

# 이제 Selenium 스크립트를 작성하고 사용할 수 있습니다.
driver.get("https://www.google.com")
print(driver.title)

# 브라우저를 닫습니다.
driver.quit()