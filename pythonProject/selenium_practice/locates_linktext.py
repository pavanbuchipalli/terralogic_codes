from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
driver = webdriver.Chrome(r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')
driver.implicitly_wait(10)
a = ActionChains(driver)
driver.implicitly_wait(3)
driver.get("https://demo.nopcommerce.com/search?q=Len")


class loca():
    def idandname(self):
        driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
        driver.find_element(By.XPATH,"//button[@class='button-1 search-box-button']").click()


    def linktext(self):
        # driver.find_element(By.LINK_TEXT,"Register").click()
        driver.find_element(By.PARTIAL_LINK_TEXT,"Reg")

ss= loca()
ss.idandname()
ss.linktext()
