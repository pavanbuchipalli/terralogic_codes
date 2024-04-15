from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class wynk():
    def __int__(self):
        driver = webdriver.Chrome()
        self.driver = driver
        self.a = ActionChains(driver)

    def login(self):
        self.__int__()
        self.driver.get("https://www.google.com/")
        self.driver.maximize_window()

    def login(self):
        self.login()
        self.driver.find_element(By.NAME, "q").send_keys("Wynk")
        self.a.send_keys(Keys.ENTER)
        self.a.perform()
        self.driver.find_element(By.XPATH,
                                 "//div[@class='yuRUbf']/a/h3[text()='Free Music Online: Play & Download MP3 Songs | Wynk Music']").click()
        self.driver.find_element(By.XPATH, "//span[@class='hover:opacity-60 cursor-pointer flex ']").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("7095626420")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(15)
        self.driver.find_element(By.XPATH, "//button[text()='Continue']").click()

        print(self.driver.title)
        time.sleep(5)

        ele = self.driver.find_element(By.XPATH, "//input[@title='Search']")
        self.a.move_to_element(ele).click()
        time.sleep(5)
        self.a.move_to_element(ele).send_keys("Telugu").click().perform()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//div[@role='tablist']/button[2]").click()

    def telugu_songs(self):
        time.sleep(2)
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        html = self.driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.DOWN)

        def press_down():
            actions = webdriver.ActionChains(self.driver)
            actions.send_keys(Keys.DOWN).perform()

        with ThreadPoolExecutor() as executor:
            for i in range(1000):
                executor.submit(press_down)

        lis_of_songs= self.driver.find_elements(By.XPATH, "//div[@class='zapSearch_zapSearchList__TvGT1']/div")
        print("Total telugu Songs", len(lis_of_songs))
        print("List Of Telugu Songs Start with R is :-")
        telugu_list = []
        for i in lis_of_songs:
            telugu_list.append(i.text.splitlines())
            # if r[0][0].startswith("R"):
        for i in range(len(telugu_list) - 1):
            if telugu_list[i][0].startswith("R"):
                print(telugu_list[i][0])


obj = wynk()
obj.telugu_songs()