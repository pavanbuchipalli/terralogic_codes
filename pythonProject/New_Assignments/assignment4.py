from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# driver = webdriver.Chrome()
# a = ActionChains(driver)


class Sports():
    def __int__(self):
        driver = webdriver.Chrome()
        self.driver = driver
        self.a = ActionChains(driver)

    def login(self):
          self.__int__()
          self.driver.get('https://olympics.com/en/')
          self.driver.maximize_window()
          self.driver.find_element(By.XPATH, "//div[@id='onetrust-button-group']/button[2]").click()
          time.sleep(5)

          self.driver.find_element(By.XPATH, '//span[text()="Sign In"]').click()
          self.driver.find_element(By.ID, "email").send_keys("pavanb1997@gmail.com")
          self.driver.find_element(By.XPATH, "//button[text()='Continue']").click()
          time.sleep(3)
          self.driver.find_element(By.ID, 'password').send_keys("Yugesh@0512")
          self.driver.find_element(By.XPATH, "//button[text()='Continue']").click()
    def Validation(self):
        self.login()
        time.sleep(4)
        actual_title = "Olympics | Olympic Games, Medals, Results & Latest News"
        Result_title = self.driver.title
        if Result_title == actual_title:
            print("Yes you are in Tokyo 2020 ")
    def sport_selection(self):
        self.Validation()

        Olympic = self.driver.find_element(By.XPATH,"//section[@class='b2p-nav__extended']/ul/li[1]/a/span")
        self.a.move_to_element(Olympic).perform()
        self.driver.execute_script("window.scrollTo(0, 20)")
        time.sleep(3)
        Tokyo = self.driver.find_element(By.XPATH, '//span[text()="Tokyo 2020"]')
        time.sleep(5)
        self.a.move_to_element(Tokyo).click().perform()
        self.driver.find_element(By.XPATH, '//ul[@data-cy="nav-dropdown"]/li[3]/a').click()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, 1200)")
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//p[text()="Badminton"]').click()
        time.sleep(5)

    def mes_double(self):
        self.sport_selection()
        Mens_double = []
        for i in range(1, 4):
            c = self.driver.find_element(By.XPATH,"//div[@data-cy='award-card-" + str(i) + "-row-1']//div[@data-cy='two-athletes-award-card']").text
            Mens_double.append(c.splitlines())
        print("Result of mens double :-", Mens_double)

    def mens_single(self):
        self.mes_double()
        self.driver.find_element(By.XPATH,"//section[@data-row-id='award-row-2']//button[@class='styles__RowToggle-sc-282810-3 lejVUA']").click()
        Mens_single = []
        for i in range(1, 4):
            c = self.driver.find_element(By.XPATH,"//div[@data-cy='award-card-" + str(i) + "-row-2']/div[@data-cy='single-athlete-award-card']").text
            Mens_single.append(c.splitlines())
        print("Result of mens single :-", Mens_single)

    def mens_mixed(self):
        self.mens_single()
        mens_mixed = []
        self.driver.find_element(By.XPATH,"//section/div/button[@class='styles__CollapseButton-sc-54gbci-3 evOjtJ']").click()
        time.sleep(5)
        for i in range(1,4):
            c = self.driver.find_element(By.XPATH,"//div[@data-cy='award-card-" + str(i) + "-row-3']/div[@data-cy='two-athletes-award-card']").text
            mens_mixed.append(c.splitlines())

        print("Result of mens mixed :-", mens_mixed)

        time.sleep(4)
    def women_double(self):
        self.mens_mixed()
        self.driver.get("https://olympics.com/en/olympic-games/tokyo-2020/results/badminton")
        women_double = []
        self.driver.find_element(By.XPATH, "//section[@data-row-id='award-row-4']/div[1]/button").click()
        time.sleep(5)
        for i in range(1, 4):
            c = self.driver.find_element(By.XPATH, "//div[@data-cy='award-card-" + str(i) + "-row-4']/div[@data-cy='two-athletes-award-card']").text
            women_double.append(c.splitlines())

        print("Result of womens_double :-", women_double)




    def women_single(self):
        self.women_double()
        self.driver.get("https://olympics.com/en/olympic-games/tokyo-2020/results/badminton")
        time.sleep(4)
        women_single = []
        self.driver.find_element(By.XPATH, "//section[@data-row-id='award-row-5']/div[1]/button").click()
        time.sleep(5)

        for i in range(1, 4):
            c = self.driver.find_element(By.XPATH,"//div[@data-cy='award-card-" + str(i) + "-row-5']/div[@data-cy='single-athlete-award-card']").text
            women_single.append(c.splitlines())
        print("Result of women_single :-", women_single)


ss = Sports()
ss.women_single()

