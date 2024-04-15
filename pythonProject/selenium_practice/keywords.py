from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()

a = ActionChains(driver)
driver.get("https://text-compare.com/")
time.sleep(10)
input1 = driver.find_element(By.XPATH,"//textarea[@name='text1']")
input2 =driver.find_element(By.XPATH,"//textarea[@name='text2']")
input1.send_keys("welcome page")

# a.key_down(Keys.CONTROL)
# a.send_keys("a")
# a.key_up(Keys.UP)
# a.perform()

# (or)
a.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

a.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

a.send_keys(Keys.TAB).perform()

a.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()