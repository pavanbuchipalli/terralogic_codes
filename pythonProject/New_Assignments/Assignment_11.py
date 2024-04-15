from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
class swiggy():
    
    def url(self):
        self.driver = webdriver.Chrome()
        self.a = ActionChains(self.driver)
        self.driver.get("https://www.google.com/")
        self.driver.maximize_window()
        #
        self.driver.find_element(By.NAME, "q").send_keys("swiggy login")
        self.a.send_keys(Keys.ENTER)
        self.a.perform()

        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//a[@class='sVXRqc']").click()

        time.sleep(5)
        self.driver.find_element(By.XPATH, '//a[@class="x4bK8"]').click()
        time.sleep(4)
        self.driver.find_element(By.ID, "mobile").send_keys("7095626420")

        self.driver.find_element(By.XPATH,'//*[@id="overlay-sidebar-root"]/div/div/div[2]/div/div/div/form/div[2]/a').click()
        self.a.send_keys(Keys.ENTER)
        self.a.perform()
        time.sleep(30)
        self.driver.find_element(By.XPATH, '//a[@class="a-ayg"]').click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "(//li[@class='_1jdR4'])[2]")
        time.sleep(10)
        print("Congratulations You login was successful", self.driver.title)

    def Top_Restarunts(self):
        self.url()
        self.driver.get('https://www.swiggy.com/city/bangalore')
        self.driver.find_element(By.XPATH, "//div[text()='Setup your precise location']").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search for area, street name...']").send_keys(
            "Koramangala")
        time.sleep(5)
        ele = self.driver.find_element(By.XPATH,
                                       '//*[text()="Locate me using GPS"]//ancestor::*[@class="style__Location-sc-zdau5c-1 fwrdJJ"]/following-sibling::div[1]')
        time.sleep(5)
        self.a.move_to_element(ele).click().perform()
        self.driver.execute_script("window.scrollTo(0, 1000)")
        print("list of Restaurants")
        for i in range(1, 11):
            time.sleep(3)
            s = "//div[@class='sc-iBdmCd hPntbc']/div[{}]//div//span[@class='sc-dmyDGi dpnlFb']".format(i)
            time.sleep(3)

            print(self.driver.find_element(By.XPATH, s).text)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='sc-iBdmCd hPntbc']/div[1]/a").click()

        r = self.driver.title
        time.sleep(5)

        items= self.driver.find_elements(By.XPATH,".//div[@id='cid-Recommended']/div[1]/div[1]//div[@class='styles_itemName__hLfgz']/h3")
        print("Recomended items of ", self.driver.title, "\n", "Count of recomended items:-", len(c))

        if len(items) == 0:
            print("The Restaurant", r, "have Zero(0) Recomanded Items so We are selecting another Restarent")
            self.driver.get(
                "https://www.swiggy.com/restaurants/chaayos-chai-snacks-relax-5th-block-koramangala-bangalore-263485")
            print("so We chose", self.driver.title, "for recomanded items")
            item2 = self.driver.find_elements(By.XPATH, "//div[@id='cid-Recommended']//h3")
            for i in item2:
                print(i.text)
        else:
            print("Recomended items of ", self.driver.title, "\n", "Count of recomended items:-", len(c))
            for i in items:
                print(i.text)


    def validation(self):
        self.Top_Restarunts()
        ADD = self.driver.find_elements(By.XPATH, "(//div[@class='main_container__3QMrw'])[1]//div[text()='ADD']")
        prices = []
        for i in ADD:
            self.driver.execute_script("window.scrollBy(0,100)")
            time.sleep(3)
            i.click()

            try:
                self.driver.execute_script("window.scrollBy(0,100)")
                time.sleep(4)
                self.driver.find_element(By.XPATH, "//span[@class='_1W_TH']").click()
                time.sleep(5)
                self.driver.find_element(By.XPATH, "//span[contains(@class,'_38xdN')]").click()
                c = self.driver.find_element(By.XPATH, "//div//span[@class='_3RJsr']").text
                digits = re.search('[0-9]*', c).group()
                prices.append(int(digits))
                time.sleep(3)

            except:
                self.driver.execute_script("window.scrollBy(0,200)")
                time.sleep(4)
                self.driver.find_element(By.XPATH, "//span[contains(@class,'_38xdN')]").click()
                c = self.driver.find_element(By.XPATH, "//div//span[@class='_3RJsr']").text
                r = re.search('[0-9]*', c).group()
                prices.append(int(r))
                time.sleep(3)
            if len(prices) == 4:
                break

        print("list of Item price", prices)
        print("Sub total before Cart", sum(prices))
        self.driver.find_element(By.XPATH, '//span[@class="_3yZyp _18ZFk"]').click()
        time.sleep(5)
        final = self.driver.find_element(By.XPATH, "//div[@class='_3ZAW1']").text
        print("sub total amount in cart", final)
        x = []
        print("Details of the tax and other Expences :-")
        self.driver.execute_script("window.scrollBy(0,250)")
        c = self.driver.find_elements(By.XPATH, "//*[contains(@class,'_3rlIu')]")
        for i in c:
            print(i.text)
        print("Validation")

        print("The Difference between  orginal price of items and price after Gst and Other taxes is :-", sum(prices) - final)


obj= swiggy()
obj.url()
obj.validation()

#Few Restarunts dont have Recommanded items so We choose chaayos which have recomended items by using try and except block