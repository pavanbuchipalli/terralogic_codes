from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome( )
driver.implicitly_wait(10)
a = ActionChains(driver)


class check():
    def lencheck(self):
        driver.get("https://itera-qa.azurewebsites.net/home/automation")
        driver.maximize_window()
        checkboxs = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
        print(len(checkboxs))

    def selectall(self):
        driver.get("https://itera-qa.azurewebsites.net/home/automation")
        driver.maximize_window()
        checkboxs = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
        print(len(checkboxs))
        for i in checkboxs:
            i.click()

    def clickselected(self):
        driver.get("https://itera-qa.azurewebsites.net/home/automation")
        driver.maximize_window()
        checkboxs = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
        print(len(checkboxs))
        for i in checkboxs:
            c =i.get_attribute("id")
            if c == "monday" or  c == "friday" :

                i.click()
    def last_2_checkbox(self):
        driver.get("https://itera-qa.azurewebsites.net/home/automation")
        driver.maximize_window()
        checkboxs = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
        for i in range(len(checkboxs)-2,len(checkboxs)):
            checkboxs[i].click()
            time.sleep(3)





ss = check()
# ss.clickselected()
# ss.selectall()
# ss.lencheck()
ss.last_2_checkbox()