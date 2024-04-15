from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
a = ActionChains(driver)

class alertss():

    def single(self):
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']").click()

        alert = driver.switch_to.alert
        print(alert.text)

        alert.accept()
    def both(self):
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']").click()

        alert = driver.switch_to.alert
        print(alert.text)

        alert.dismiss()

    def inpt(self):
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()

        alert = driver.switch_to.alert
        print(alert.text)
        alert.send_keys("welcome")

        alert.accept()

ss =alertss()
ss.single()
time.sleep(2)
