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
driver = webdriver.Chrome()

driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.NAME,"q").send_keys("Gmail")
time.sleep(10)
driver.find_element()