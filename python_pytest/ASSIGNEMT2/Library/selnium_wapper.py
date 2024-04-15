
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Seleniumwapper:
    def __init__(self,driver):
        self.driver = driver

    def click_element(self, element):
        self.driver.find_element(element[0], element[1]).click()

    def enter_element(self, element, text):
        self.driver.find_element(element[0],element[1]).send_keys(text)

    def title_extraction(self):
        Result_title = self.driver.title
        assert Result_title == "Inbox - qq6630685@gmail.com - Gmail"
        print("congratulations successfully login")
        # assert Result_title != "Inbox - qq6630685@gmail.com - Gmail"
        # print("You have not login ")

    def sent_mails(self,element):
        self.driver.find_element(element[0],element[1]).click()

    def take_data_of_sent_mails(self,element):
        count = self.driver.find_element(element[0],element[1]).text
        print("Total Number of sent emails is ", count)

    def all_settings(self,element):
        self.driver.find_element(element[0], element[1]).click()


