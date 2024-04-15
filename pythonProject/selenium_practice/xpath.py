from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
driver = webdriver.Chrome(r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')

class xpatth():
    def absolut(self):
        driver.get("https://www.facebook.com/")
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("pavan")
        time.sleep(3)


    def relative(self):
        driver.get("https://www.facebook.com/")
        driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("pavanb1997")
        time.sleep(3)


ss =xpatth()
ss.relative()
