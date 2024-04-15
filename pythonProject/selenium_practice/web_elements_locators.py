from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
driver = webdriver.Chrome(r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')
driver.implicitly_wait(10)
a = ActionChains(driver)

driver.get("https://www.redbus.in/bus-tickets?psafe_param=1&gclid=EAIaIQobChMI7Yyi9IOh_gIVln8rCh2QdgO-EAAYASAAEgLHJPD_BwE")

driver.maximize_window()
class elements():

    def tagname(self):
        c =driver.find_elements(By.TAG_NAME,"a")
        print(len(c))


    def classname(self):

        c =driver.find_elements(By.CLASS_NAME,"D121_options_nav options-nav mob-hide")
        print(len(c))

ss= elements()
ss.tagname()
ss.classname()
driver.close()


