from selenium import webdriver
from selenium.webdriver.common import keys
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
driver.get("https://www.foundit.in/")

time.sleep(3)
driver.find_element(By.XPATH,"//div[contains(text(),'Upload Resume')]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys(r"C:\Users\PavanB-3247\PycharmProjects\pythonProject\New_Assignments\sample.txt")
time.sleep(5)