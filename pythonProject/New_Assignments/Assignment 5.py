from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Webseries():
    def __int__(self):
        driver = webdriver.Chrome()
        self.driver = driver
        self.a = ActionChains(driver)
    def Webseries_duration(self):
        self.__int__()
        self.driver.get("https://www.google.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        time.sleep(5)
        self.driver.find_element(By.NAME, "q").send_keys("Netflix")
        self.a.send_keys(Keys.ENTER)

        self.a.perform()
        self.driver.find_element(By.XPATH, "//h3[text()='Netflix - Watch TV Shows Online, Watch Movies Online']").click()

        self.driver.find_element(By.XPATH, "//a[text()='Sign In']").click()

        self.driver.find_element(By.XPATH, "//input[@id='id_userLoginId']").send_keys("*************")

        self.driver.find_element(By.XPATH, "//input[@id='id_password']").send_keys("********")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "(//div[@class='avatar-wrapper'])[1]").click()
        time.sleep(3)
        search = self.driver.find_element(By.XPATH, "//button[@aria-label='Search']")
        self.a.move_to_element(search).click().send_keys("Money Heist").click().perform()

        time.sleep(3)
        ele = self.driver.find_element(By.XPATH, "(//div[@class='boxart-size-16x9 boxart-container boxart-rounded'])[1]")

        self.a.move_to_element(ele).click().perform()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//div[@class='episodeSelector-dropdown']//div[@class='ltr-1bbjknu']/button").click()
        time.sleep(3)
        ele2 = self.driver.find_element(By.XPATH, "//li[text()='See All Episodes']")
        self.a.move_to_element(ele2).click().perform()
        time.sleep(10)
        list_of_time = []
        total_duration = self.driver.find_elements(By.XPATH,
                                              "//div[@class='titleCardList-title']//span[@class='duration ellipsized']")
        for single_episode in total_duration:
            convert = (str(single_episode.text)).replace("m", "")
            list_of_time.append(int(convert))
        print("The Total Duration of the Money heist Web Series is :- ", sum(list_of_time), "Mins")


    def Awards(self):
        self.__int__()
        self.Webseries_duration()
        time.sleep(5)
        self.driver.get("https://www.google.com/")
        self.driver.maximize_window()

        self.driver.find_element(By.NAME, "q").send_keys("money heist")
        self.a.send_keys(Keys.ENTER)
        self.a.perform()
        self.driver.find_element(By.XPATH, "//h3[text()='Money Heist']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Awards and nominations']").click()
        # time.sleep(4)
        ele = self.driver.find_element(By.XPATH,"//table[@class='wikitable sortable plainrowheaders jquery-tablesorter']//th[5]")
        self.a.double_click(ele).perform()
        # time.sleep(5) 
        c = self.driver.find_elements(By.XPATH,"//table[@class='wikitable sortable plainrowheaders jquery-tablesorter']/tbody/tr/td[contains(text(), 'Won')]")
        cc = []
        print("Number of awards won by money heist", len(c))
        print("List of Awards :")
        for i in range(1, len(c)):
            years = "//table[@class='wikitable sortable plainrowheaders jquery-tablesorter']/tbody/tr[{}]/th".format(i)
            year = self.driver.find_element(By.XPATH, years).text
            Awards = "//table[@class='wikitable sortable plainrowheaders jquery-tablesorter']/tbody/tr[{}]/td[1]".format(i, i)
            Award = self.driver.find_element(By.XPATH, Awards).text
            categorys = "//table[@class='wikitable sortable plainrowheaders jquery-tablesorter']/tbody/tr[{}]/td[2]".format(i)
            category = self.driver.find_element(By.XPATH, categorys).text
            Results = "//table[@class='wikitable sortable plainrowheaders jquery-tablesorter']/tbody/tr[{}]/td[4]".format(i)
            result = self.driver.find_element(By.XPATH, Results).text

            print("Year of Award won :- ", year, "\n" "Award name :-", Award, "\n""Award category:-", category,
                  "\n""Result Of Award:-", result)
            print(
                "-------------------------------------------------------------------------------------------------------------------------")



ss = Webseries()

ss.Awards()


