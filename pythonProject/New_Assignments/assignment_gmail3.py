from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

import time


class gmail_login():
    def __int__(self):
        driver = webdriver.Chrome()
        self.driver = driver
        self.a = ActionChains(driver)

    def credntials(self):

        self.driver.get(
            "https://accounts.google.com/v3/signin/identifier?dsh=S-1610540532%3A1683214706950646&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=Af_xneH8_BvaZbOEwfLu2dQI7Ws4SKgmfv7Kc91HMWT5qwJS7aLQ8dKb-ghP6sFPVQgMqqoa6zlpjw&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
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
        time.sleep(3)

        self.driver.find_element(By.XPATH,'//a[@class="gb_d gb_Aa gb_D"]').click()
        time.sleep(3)
