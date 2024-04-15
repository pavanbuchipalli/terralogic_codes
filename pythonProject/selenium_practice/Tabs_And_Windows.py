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
# driver.get("https://demo.nopcommerce.com/")
#
# regcli= Keys.CONTROL+Keys.ENTER
# driver.find_element(By.XPATH,"//a[text()='Register']").send_keys(regcli)
# time.sleep(5)


# swith to new window in selenium4
# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.new_window("Tab")
# driver.get("https://demo.nopcommerce.com/")


#switch to new browser window
# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.new_window("window")
# driver.get("https://demo.nopcommerce.com/")
# time.sleep(10)