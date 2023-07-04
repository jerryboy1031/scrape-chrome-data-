from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from urllib.request import urlopen

driver_path = "/chromedriver_win32/chromedriver.exe" # the path of chromedriver.exe
service= Service(driver_path)
option = Options()
#操作網頁是不顯示網頁 manipulate the browser invisibly
#option.add_argument("-headless")
chrome = webdriver.Chrome(service=service, options=option)
chrome.get("https://www.facebook.com/")

email = chrome.find_element("id", "email")
password = chrome.find_element("id", "pass")

time.sleep(1)
email.send_keys('jerryboy1031@yahoo.com.tw')
password.send_keys('zxcvbnm1031')
time.sleep(3)
password.submit()
time.sleep(5)
#關閉瀏覽器 close the browser
chrome.close()