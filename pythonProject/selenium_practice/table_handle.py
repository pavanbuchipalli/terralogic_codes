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

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
c = len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr'))
d = len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr[1]/th'))
print(c,d)
#if u want to print author names
no = driver.find_elements(By.XPATH,"//table//tr/td[2]")
for i in range(2,len(no)+1):
    c = driver.find_element(By.XPATH,"//table//tr["+str(i)+"]/td[2]").text
    print(c)


#if u want book name whos is author mukesh
no = driver.find_elements(By.XPATH,"//table//tr/td[2]")
for i in range(2,len(no)+1):
    c = driver.find_element(By.XPATH,"//table//tr["+str(i)+"]/td[2]").text
    if c =="Mukesh":
        time.sleep(3)
        r = driver.find_element(By.XPATH,"//table//tr["+str(i)+"]/td[1]]").text
        # f =driver.find_element(By.XPATH,"//table//tr["+str(i)+"]/td[2]").text
        print(c,r)