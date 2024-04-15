from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class cource():
    def __int__(self):
        driver = webdriver.Chrome()
        self.driver = driver
        self.a = ActionChains(driver)

    def login(self):
        self.__int__()
        self.driver.get('https://www.letskodeit.com/courses')
        self.driver.maximize_window()

    def cource_name(self):
        self.login()
        self.driver.find_element(By.XPATH,'//ul[@class="nav navbar-nav pull-center dynamic_menu_texts"]/li[3]').click()


        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

        courses =self.driver.find_elements(By.XPATH,'//div//h4[@class="dynamic-heading"]')


        print("List of courses in letskodeitcom\n")
        print("Count of Courses",len(courses))
        for course  in courses :

            print(course.text)




ss =cource()
ss.cource_name()