"""
게시글의 커버 이미지를 조회
"""

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time
import config
import requests

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


# service = Service(config.ABSOLUTE_CHROME_DRIVER_PATH)
# driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(options=options)


driver.get('https://gall.dcinside.com/mini/board/lists?id=vuta')

page = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//body")))


cover_img = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//span[@class='cover']"))
)

img_style = cover_img.get_attribute('style')

start = img_style.find('url(') + 4  # url( 시작 위치에서 '(' 다음 위치를 계산
end = img_style.find(')', start)    # ')' 위치를 찾습니다.

url = img_style[start:end].strip('"')  # 양 끝의 쌍따옴표 제거

response = requests.get(url)

print(url)

if response.status_code == 200:
    # 이미지 데이터를 'image.png' 파일로 저장합니다.
    with open('image.png', 'wb') as file:
        file.write(response.content)
