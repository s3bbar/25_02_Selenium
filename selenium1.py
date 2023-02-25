from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument("--headless=new")
ser = Service(r"/usr/bin/chromedriver")
op = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=ser, options=op)
time.sleep(1)

driver.get('https://google.com')
print('Nazwa strony', driver.title)
time.sleep(2)
button1_accept = driver.find_element('id','L2AGLb')
button1_accept.click()
search_field = driver.find_element('name','q')
search_field.send_keys('Czy jutro jest niedziela handlowa?')
search_button = driver.find_element('name', 'btnK')
search_button.submit()
time.sleep(3)

driver.close()