import time
from selenium import webdriver
#object of ChromeOptions class
c = webdriver.ChromeOptions()
#incognito parameter passed
c.add_argument("--incognito")
#set chromodriver.exe path
driver = webdriver.Chrome()
# driver.implicitly_wait(0.5)

#launch URL
driver.get("https://www.tutorialspoint.com/tutor_connect/index.php")

time.sleep(20)