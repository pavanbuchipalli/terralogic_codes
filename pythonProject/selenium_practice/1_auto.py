from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')
a = ActionChains(driver)
class auto:
    def text(self):

        driver.get('https://www.redbus.in/bus-tickets?psafe_param=1&gclid=EAIaIQobChMI7Yyi9IOh_gIVln8rCh2QdgO-EAAYASAAEgLHJPD_BwE')
        # driver.maximize_window()
        titl = driver.title
        print(titl)
    def booking(self):
        driver.find_element(By.XPATH,"//input[@type='text' and  @id='txtSource']").send_keys("Madanapalli")
        # c =a.move_to_element("//div[text()='Madanapalli']")
        driver.find_element(By.XPATH,'//input[@type="text" and @id="txtDestination"]').send_keys("Bangalore")
        
        driver.close()
cc=auto()
cc.text()
cc.booking()


