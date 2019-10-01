
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome('./chromedriver')
driver.get('http://www.office.kobe-u.ac.jp/stdnt-kymsys/student/student.html')
driver.find_element_by_xpath('//*[@id="uribo_net"]/h2/a/img').click()
adress = driver.find_element_by_xpath('//*[@id="j_username"]')
adress.send_keys('1774376t') #自分の学籍番号
password = driver.find_element_by_xpath('//*[@id="j_password"]')
password.send_keys('=H2BarQq') #自分のパスワード
driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr/td[1]/div/form/table/tbody/tr[3]/td/input').click()
