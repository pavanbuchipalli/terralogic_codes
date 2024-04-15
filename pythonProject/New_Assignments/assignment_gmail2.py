import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

from New_Assignments.assignment_gmail1 import gmail_login


class sent_data(gmail_login):
    def __init__(self, driver):
        self.driver=driver



    def gmail_sent_email(self):

        driver.find_element(By.XPATH, "//div[@class='TN bzz aHS-bnu']").click()
        # time.sleep(10)
        # driver.find_element(By.XPATH,'//span[@class="y5Iqsb Voigeb vZvJBb"]').click()
        time.sleep(4)
        v =self.driver.find_element(By.XPATH,'(//span[@class="ts"])[6]').text
        print("Total Number of sent emails is ",v)
driver=webdriver.Chrome()
obj2 =sent_data(driver)
obj2.credntials()
obj2.gmail_sent_email()



