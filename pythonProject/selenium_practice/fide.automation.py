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

driver.get("https://fide.com/")
driver.maximize_window()
driver.find_element(By.XPATH,'//li[@class="nav-item"]//a[text()="Ratings"]').click()
driver.find_element(By.XPATH,'//div[@class="rectangle-menu"]//a[1]').click()
c = driver.find_elements(By.XPATH,'//section[@class="container section-profile"]/div[4]/table/tbody/tr')
print(len(c))
time.sleep(5)