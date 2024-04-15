from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')
driver.implicitly_wait(10)
a = ActionChains(driver)
mywait =WebDriverWait(driver,10)


driver.get("https://www.google.com/")
time.sleep(3)
searchbox = driver.find_element(By.XPATH,"//textarea[@role='combobox']")
searchbox.clear()
searchbox.send_keys("Terralogic")
searchbox.submit()
mywait.until(EC.presence_of_element_located(By.XPATH,"//a[normalize-space()='USA']"))