from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')
a = ActionChains(driver)
class auto:
    def text(self):

        driver.get('https://www.hyrtutorials.com/p/calendar-practice.html')
        driver.maximize_window()
        titl = driver.title
        print(titl)
        try:
            driver.find_element(By.ID, 'second_date_picker').click()
            driver.find_element(By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody/tr/td/a[text()='15']").click()
        except:
            print("exception")


        time.sleep(2)
    # def booking(self):

cc = auto()
cc.text()
#cc.booking()
