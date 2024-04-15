import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Gmail():
        def __int__(self):
            driver = webdriver.Chrome()
            self.driver = driver
            self.a = ActionChains(driver)
        def login(self):
            self.__int__()
            self.driver.get("https://www.google.com/")
            self.driver.maximize_window()
        def valid_invalid_login(self):
            self.login()
            self.driver.find_element(By.NAME, "q").send_keys("Gmail")
            self.a.send_keys(Keys.ENTER)
            self.a.perform()
            time.sleep(4)
            self.driver.find_element(By.XPATH, '//h3[text()="Gmail - Google"]').click()
            self.driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-1610540532%3A1683214706950646&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=Af_xneH8_BvaZbOEwfLu2dQI7Ws4SKgmfv7Kc91HMWT5qwJS7aLQ8dKb-ghP6sFPVQgMqqoa6zlpjw&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            self.driver.find_element(By.ID, 'identifierId').send_keys("qq6630685@gmail.com")
            self.driver.find_element(By.XPATH, '//span[text()="Next"]').click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//input[@name="Passwd"]').send_keys("Yugesh@05")
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//span[text()='Next']").click()
            time.sleep(5)
            Result_title = self.driver.title
            Expected_tile = "Inbox - qq6630685@gmail.com - Gmail"
            if Result_title == Expected_tile:
                print("congratulations You successfully login to Gmail  ")
            else:
                error = self.driver.find_element(By.XPATH, '//div[@jsname="B34EJ"]/span')
                print(error.text)

            self.driver.close()


ss =Gmail()
ss.valid_invalid_login()





#