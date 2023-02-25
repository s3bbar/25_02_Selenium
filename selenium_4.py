from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as excon
from selenium.webdriver.support.wait import WebDriverWait


def czekaj_na_id(element_id):
    timeout = 5
    timeout_message = f"Element o id {element_id} nie pojawił się w czasie {timeout}"
    lokalizator = {By.ID, element_id}
    znaleziono = excon.visibility_of_element_located(lokalizator)
    oczekiwator = WebDriverWait(driver, timeout)
    return oczekiwator.until(znaleziono, timeout_message)


#options = Options()
#options.add_argument("--headless=new")
#ser = Service(r"/usr/bin/chromedriver")
#op = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=ser, options=op)
driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com/')
print('Nazwa strony', driver.title)

try:
    login_button = czekaj_na_id('login_button')
except TimeoutException:
    print('Nie znaeziono')
else:
    print('Znaleziono')
finally:
    pass



