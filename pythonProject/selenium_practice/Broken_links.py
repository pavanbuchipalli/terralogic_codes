from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
driver = webdriver.Chrome( )
driver.implicitly_wait(10)
a = ActionChains(driver)


driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
links = driver.find_elements(By.TAG_NAME,"a")
count = 0


for link in links:
    url = link.get_attribute("href")
    try:

        res =requests.head(url)
    except:
          None


    if  res.status_code >= 400 :
        print(url,"it is is broken link")
        count += 1
    print(count)
