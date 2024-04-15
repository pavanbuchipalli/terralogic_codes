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

a = ActionChains(driver)
driver.get("https://jqueryui.com/slider/")
time.sleep(10)
min = driver.find_element(By.XPATH,"//div[@id='slider']")
print(min.location)
a.drag_and_drop_by_offset(min,100,0).perform()