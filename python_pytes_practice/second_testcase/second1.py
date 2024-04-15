import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
a = ActionChains(driver)

def testfirst1():
    driver.get("https://www.browserstack.com/guide/alerts-and-popups-in-selenium")
    time.sleep(3)
    # print(driver.title)
    return "this is first function"



obj =testfirst1()
print(obj)