from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
a = ActionChains(driver)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(3)
driver.add_cookie({"name":"dsfds","value":"12454576"})
cookies = driver.get_cookies()
print(len(cookies))
for i in cookies:
    # print(i)
    print(i.get("name"))
driver.delete_cookie("dsfds")
cookiess = driver.get_cookies()
print(len(cookiess))

