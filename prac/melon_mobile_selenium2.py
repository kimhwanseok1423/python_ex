from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
options=Options()

#실행시 화면맥스
options.add_argument("--start-maximized")

# 자동꺼짐 방지
options.add_experimental_option("detach",True)


# 터미널에서 불필요한 메시지 출력 하지 않기 위해
options.add_experimental_option("excludeSwitches",["enable-logging"])

# 멜론 모바일 설정위해 아이폰 설정후 가져옴
user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"

## user agent의 크롬버전을 낮추거나 바꾸고싶을때 user_agent에서 버전만 낮추고 실행시 개발자 도구에서 적용된 버전으로 실행됨
options.add_argument(f"user-agent={user_agent}")


service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=options)
url="https://m2.melon.com/index.htm"

driver.get(url)
time.sleep(2)

#현재 주소를 알아내는것
print(driver.current_url)

if driver.current_url != url:
    driver.get(url)
    time.sleep(2)

#배너가 뜨는경우 그 클래스나 id의 코드를 보고 닫으면됨


## 방법2  top100을 묶은 _chartList라는 id가 없는경우 가져오는법

driver.find_element(By.LINK_TEXT,"멜론차트").click()
time.sleep(2)
driver.find_elements(By.ID,"moreBtn")[1].click()
time.sleep(2)


items=driver.find_elements(By.CLASS_NAME,"list_item")

# for문돌리는데 예를들어 2번이 ranking_num이없다? nosuchelement 실행 > 우리가 필요로하는 정보를 가지고있지않으므로 item을 items리스트에서 지우기
# items[:]는 복사본 만들어서 순번꼬임방지
for item in items[:]:
    try:
        ranking_num=item.find_element(By.CLASS_NAME,"ranking_num")
    except NoSuchElementException:
        print("랭크가 없어서 삭제합니다.")
        items.remove(item)

print(len(items))
driver.quit()