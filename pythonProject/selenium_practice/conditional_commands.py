from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

class conditional():

    def enabled(self):

        driver = webdriver.Chrome(r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')

        driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
        cc = driver.find_element(By.ID,"FirstName")
        print(cc.is_enabled())
        driver.close()

    def disabled(self):
        driver = webdriver.Chrome(r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')

        driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
        cc = driver.find_element(By.ID, "FirstName")
        print(cc.is_displayed())
        driver.close()

    def selected(self):
        driver = webdriver.Chrome(r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')
        driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
        rr = driver.find_element(By.ID,"gender-male")
        print(rr.is_selected())
        driver.close()



ss= conditional()
ss.disabled()
ss.enabled()
ss.selected()
