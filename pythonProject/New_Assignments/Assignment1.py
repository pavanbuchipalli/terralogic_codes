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

a.send_keys(Keys.ENTER)
a.perform()
driver.find_element(By.XPATH,"//h3[text()='Gmail - Google']").click()
driver.find_element(By.XPATH,"//a[text()='Sign in']").click()
driver.find_element(By.ID,"identifierId").send_keys("pavanb1997")
driver.find_element(By.XPATH,"//span[text()='Next']").click()
time.sleep(100)
time.sleep(8)