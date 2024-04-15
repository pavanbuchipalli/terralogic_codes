from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome(r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')
class methods():
   def or_oper(self):
       driver.get("https://www.facebook.com/")
       driver.find_element(By.XPATH,"//input[@class='inputtext _55r1 _6luy' or @type='ext']").send_keys("pavanb1997")
       time.sleep(3)

   def and_oper(self):
       driver.get("https://www.facebook.com/")
       driver.find_element(By.XPATH,"//input[@class='inputtext _55r1 _6luy' or @type='text']").send_keys("pavanb199")
       time.sleep(3)

   def contains(self):
       driver.get("https://www.facebook.com/")
       driver.find_element(By.XPATH, "//input[contains( @ id, 'email')]").send_keys("pavanb199")
       time.sleep(3)


   def start_with(self):
       driver.get("https://www.facebook.com/")
       driver.find_element(By.XPATH,"//input[starts-with(@id,'e')]").send_keys("pavanb19")
       time.sleep(3)



ss =methods()
ss.start_with()