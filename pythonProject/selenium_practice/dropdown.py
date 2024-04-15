from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
a = ActionChains(driver)


class drop_down():

    def by_value(self):
        driver.get("https://www.opencart.com/index.php?route=account/register")
        driver.implicitly_wait(10)
        driver.maximize_window()
        dropdown = Select(driver.find_elements(By.XPATH,'//select[@id="input-country"]'))

        dropdown.select_by_value("American Samoa")
        all_options = dropdown.options
        print(len(all_options))

        for opt in all_options:
            print(opt.text)


# dropdown.select_by_index()
# dropdown.select_by_visible_text()

ss = drop_down()
ss.by_value()

time.sleep(3)
