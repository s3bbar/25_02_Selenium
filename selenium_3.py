import datetime

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def make_screenshot(driver):
    teraz = datetime.datetime.now()
    screenshot = 'screenshot' + teraz.strftime('_%H%M%S') + '.png'
    driver.get_screenshot_as_file(screenshot)


options = Options()
options.add_argument("--headless=new")
ser = Service(r"/usr/bin/chromedriver")
op = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=ser, options=op)
driver.get('https://www.saucedemo.com/')
print('Nazwa strony', driver.title)
time.sleep(1)

try:
    username_field = driver.find_element('id', 'user-name')
    username_field.clear()
    username_field.send_keys('standard_user')
except:
    make_screenshot(driver)

password_field = driver.find_element('id', 'password')
password_field.clear()
password_field.send_keys('secret_sauce')

login_button = driver.find_element('name', 'login-button')
login_button.click()

time.sleep(2)

driver.quit()
