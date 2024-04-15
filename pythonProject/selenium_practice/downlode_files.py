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

import os
location = os.getcwd()
print(location)
preference ={"download.default_directory":location,"pulgins.always_open_pdf_externally":True}
ops = webdriver.ChromeOptions
ops.add_experimental_option("prefs" ,{"download.default_directory":location})
driver = webdriver.Chrome(options=ops)

a = ActionChains(driver)
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
time.sleep(10)


driver.find_element(By.XPATH,"(//a[contains(text(),'Download sample DOC file')])[1]").click()

gotit=driver.find_element(By.ID,'accept-cookie-notification')

gotit.click();
time.sleep(10)