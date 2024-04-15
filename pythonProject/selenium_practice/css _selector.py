from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
driver = webdriver.Chrome(r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')
driver.implicitly_wait(10)
a = ActionChains(driver)


class face():
    def tag_and_id(self):
        driver.get("https://www.facebook.com/")
        driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("pavan")

    def tag_and_class(self):
        driver.get("https://www.facebook.com/")
        driver.find_element(By.CSS_SELECTOR,"input.inputtext ").send_keys("pacavn")


    def tag_and_attribute(self):
        driver.get("https://www.facebook.com/")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("pabvhbh")

    def tag_class_attribute(self):
        driver.get("https://www.facebook.com/")
        driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_email]").send_keys("pabv0000h")


ss = face()
ss.tag_class_attribute()
driver.close()


time.sleep()
driver.close()
