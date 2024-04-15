from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
driver = webdriver.Chrome(r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')



driver.get("https://money.rediff.com/index.html")
class xpath():

    def child(self):
        cc =driver.find_element(By.XPATH,'//div[@class="rediffgurus"]//child::h2[1]').text
        print(cc)
        driver.close()
    def parent_and_following(self):

        cc =driver.find_element(By.XPATH,'//a[contains(text(),"S&P BSE Sensex")]/parent::li').text
        print(cc)
    def childs(self):
        cc =driver.find_elements(By.XPATH,'//a[contains(text(),"S&P BSE Sensex")]/ancestor::ul/child::li')
        print(len(cc))
ss =xpath()
ss.childs()

