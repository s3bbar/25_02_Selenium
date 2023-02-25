from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as excon
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument("--headless=new")
ser = Service(r"/usr/bin/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get('https://www.saucedemo.com/')
print('Nazwa strony', driver.title)

element_id = 'login-button'
timeout = 10
timeout_message = f"Element o id {element_id} nie pojawił się w czasie {timeout}"
lokalizator = {By.ID, element_id}
znaleziono = excon.visibility_of_element_located(lokalizator)
oczekiwator = WebDriverWait(driver, timeout)


