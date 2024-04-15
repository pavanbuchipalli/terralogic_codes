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



driver.get('https://jqueryui.com/datepicker/')
driver.switch_to.frame(0)
driver.find_element(By.ID,'datepicker').send_keys("05/30/2023")
time.sleep(10)
months= "October"
years = "2022"
day = "22"

while True:
    month = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    year = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if month == months and year == years :
        break
    else:
        driver.find_element(By.XPATH,"//span[text()='Prev']").click()

        # '// a[ @class ="ui-datepicker-prev ui-corner-all"]
date = driver.find_elements(By.XPATH,"//table//tr/td/a")
for i in date :
    if i == day :
        i.click()
        break
time.sleep(10)