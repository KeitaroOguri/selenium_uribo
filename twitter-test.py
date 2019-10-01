
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import chromedriver_binary
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
driver.get('https://twitter.com/')
time.sleep(5)
login = driver.find_element_by_class_name('StaticLoggedOutHomePage-input')
login.click()
adress = driver.find_element_by_class_name('js-username-field')
adress.send_keys('compassvision01@gmail.com')
password = driver.find_element_by_class_name('js-password-field')
password.send_keys('8kikuzato8K')
driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()
time.sleep(5)
driver.quit()
