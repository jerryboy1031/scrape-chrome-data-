from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from urllib.request import urlopen

option = Options()
#操作網頁是不顯示網頁 manipulate the browser invisibly
#option.add_argument("-headless")

driver_path = "./chromedriver_win32/chromedriver.exe"
chrome = webdriver.Chrome(driver_path, options=option)
chrome.get("https://www.facebook.com/")

email = chrome.find_element("id", "email")
password = chrome.find_element("id", "pass")

time.sleep(5)
email.send_keys('jerryboy1031@yahoo.com')
password.send_keys('zxcvbnm1031')
password.submit()

#關閉瀏覽器 close the browser
#chrome.close()