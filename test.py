
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import chromedriver_binary
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.google.com/')
time.sleep(5)
search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)
driver.quit()
