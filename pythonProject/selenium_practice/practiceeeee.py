from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
driver = webdriver.Chrome()


a = ActionChains(driver)
driver.get("https://www.swiggy.com/restaurants/asha-tiffins-7th-sector-hsr-layout-bangalore-201224")
time.sleep(30)
c = driver.find_elements(By.XPATH,"//div[text()='ADD']")
for i in  c:
    i.click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//span[text()='Add Item']").click()
    time.sleep(2)