from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
a = ActionChains(driver)
class login():
    def org(self):
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        driver.maximize_window()


    def logiin(self):
        time.sleep(5)
        driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active' and @type='password' ]").send_keys("admin123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()


    def asse(self):
        present_title = driver.title
        expected_title = "OrangeHRM"
        if present_title == expected_title :
            print("yes title is same ")
        time.sleep(3)
        driver.close()

ss = login()
ss.org()
ss.logiin()
ss.asse()