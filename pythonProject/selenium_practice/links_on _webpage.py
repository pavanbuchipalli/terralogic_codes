from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
a = ActionChains(driver)


class links():


    def full_link(self):
        driver.get("https://www.nopcommerce.com/en")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, "Download nopCommerce").click()
        time.sleep(1)
        driver.close()

    def partial(self):
        driver.get("https://www.nopcommerce.com/en")
        driver.maximize_window()
        driver.find_element(By.PARTIAL_LINK_TEXT, "Download").click()
        time.sleep(1)
        driver.close()

    def all_links(self):
        driver.get("https://www.nopcommerce.com/en")
        driver.maximize_window()
        c = driver.find_elements(By.TAG_NAME,"a")
        print(len(c))
        for i in c:
            print(i.text)




ss = links()
ss.all_links()
