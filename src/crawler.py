from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# service = Service(config.ABSOLUTE_CHROME_DRIVER_PATH)
# driver = webdriver.Chrome(service=service, options=options)

def start_driver():
  return webdriver.Chrome(options=options)

def find_page(url: str, locator: str, wait_time: int = 5):
  driver = start_driver()
  driver.get(url)

  return  WebDriverWait(driver, wait_time).until(
      EC.presence_of_element_located((By.XPATH, locator))
  )
