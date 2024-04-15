from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
class appcommands():
    def title(self):
        driver = webdriver.Chrome(r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')
        cc = driver.title
        print(cc)
        driver.close()

    def url(self):
        driver = webdriver.Chrome(r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')
        driver.get("https://www.browserstack.com/guide/alerts-and-popups-in-selenium")
        ss = driver.current_url

        print(ss)
        driver.close()
ee =appcommands()
ee.title()
ee.url()

