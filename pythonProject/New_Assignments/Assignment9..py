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

class Redbus():

    def url(self):
        self.driver = webdriver.Chrome()
        self.driver = self.driver
        self.a = ActionChains(self.driver)
        ch = Options()
        ch.add_argument("--disable-notifications")

    def Create_Account(self):
        self.url()
        self.driver.get("https://www.google.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME, "q").send_keys("Redbus")
        self.a.send_keys(Keys.ENTER)
        self.a.perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[text()='Bus Ticket Booking Online']").click()
        time.sleep(3)
        print(self.driver.title)

        self.driver.find_element(By.XPATH, "//span[@class='D121_options_nav_a']").click()
        time.sleep(4)
        s = self.driver.find_element(By.XPATH, "//span[text()='Sign In/Sign Up']")
        self.a.move_to_element(s).click()
        self.a.perform()
        time.sleep(10)

        outer_frame = self.driver.find_element(By.XPATH, "//iframe[@class='D121_iframe']")
        self.driver.switch_to.frame(outer_frame)
        time.sleep(5)
        parent = self.driver.current_window_handle
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[7]/div/div").click()
        time.sleep(3)

        windows = self.driver.window_handles
        for child in windows:
            if parent != child:
                self.driver.switch_to.window(child)
                print(self.driver.title)
                self.driver.find_element(By.ID, 'identifierId').send_keys("qq6630685@gmail.com")
                self.driver.find_element(By.XPATH, '//span[text()="Next"]').click()
                time.sleep(5)
                self.driver.find_element(By.XPATH, '//input[@name="Passwd"]').send_keys("Yugesh@05")
                time.sleep(5)
                self.driver.find_element(By.XPATH, "//span[text()='Next']").click()
                time.sleep(5)
                self.driver.switch_to.window(parent)
                time.sleep(3)
                self.driver.switch_to.frame(outer_frame)
                time.sleep(3)
                gg = self.driver.find_element(By.XPATH, "//input[@id='mobileNo']")
                gg.click()
                gg.send_keys("8328481226")
                time.sleep(3)
                self.driver.find_element(By.XPATH, "//button[@id='sendOTP']").click()
                time.sleep(5)
                print(self.driver.title)

    def login(self):
        self.url()
        self.driver.get("https://www.redbus.in/")
        time.sleep(3)
        ele = self.driver.find_element(By.ID, "src")
        self.a.move_to_element(ele).click().send_keys("Bangalore").send_keys(Keys.ENTER)
        time.sleep(5)
        ele = self.driver.find_element(By.ID, "dest")
        self.a.move_to_element(ele).click().send_keys("Hyderabad").click().perform()
        time.sleep(1)
        ele2 = self.driver.find_element(By.ID, "onward_cal")
        self.a.move_to_element(ele2).click().perform()
        time.sleep(4)
        ele2 = self.driver.find_element(By.XPATH, "//table/tbody/tr[4]/td[7]")
        self.a.move_to_element(ele2).click().perform()
        time.sleep(3)
        self.driver.find_element(By.ID, "search_btn").click()
        time.sleep(10)
    def route(self):
        self.login()
        time.sleep(5)
        # self.driver.get("https://www.redbus.in/bus-tickets/bangalore-to-hyderabad?fromCityName=Bangalore&fromCityId=122&toCityName=Hyderabad&toCityId=124&onward=15-May-2023&srcCountry=IND&destCountry=IND&opId=0&busType=Any")
        # time.sleep(5)
        print(self.driver.title)
        aa = self.driver.find_element(By.XPATH, "//i[@class='icon icon-close']")
        self.a.move_to_element(aa).click().perform()
        c = self.driver.find_element(By.XPATH, "//span[@class='f-bold busFound']").text
        print("Total Number of buses:-", c)
        self.driver.execute_script("window.scrollBy(0,250)")
        time.sleep(10)

        self.driver.find_element(By.XPATH, "(//div[@class='clearfix bus-item'])[1]/div[2]/div[1]").click()
        time.sleep(10)
        s = self.driver.find_element(By.XPATH, "(//div[@class='clearfix row-one'])[1]/div[7]//div[1]").text
        print("starting  price on the ticket ",s)
        time.sleep(5)
        l = []
        for i in range(2, 8):
            r = self.driver.find_element(By.XPATH, "//ul[@class='clearfix discountPrice']/li[" + str(i) + "]").text
            l.append(r)
        print("list of price of seats",l)
        time.sleep(10)
        e = self.driver.find_element(By.XPATH, "//canvas[@data-type='lower']")
        self.a.move_to_element_with_offset(e, 39, 39).click().perform()
        time.sleep(5)
        original_price = self.driver.find_element(By.XPATH, '(//span[@class="fr fare-summary-value"]/span)[4]').text
        v = re.search("\d*", original_price).group()
        print(v)
        time.sleep(4)
        original_price = int(v)
        print("original price of ticket is ", original_price)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "(//div[@class='radio-css '])[1]").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "(//div[@class='radio-css '])[31]").click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, "//div[@class='continue-container w-100 fl m-b-10']/button").click()
        time.sleep(10)
        actions = self.a.send_keys(Keys.TAB).send_keys("pavan")
        actions.perform()
        time.sleep(5)
        self.driver.find_element(By.ID, "div_22_0").click()
        time.sleep(5)
        age = self.driver.find_element(By.XPATH, "//input[@id='seatno-01']")
        self.a.move_to_element(age).click().send_keys("25").perform()
        time.sleep(10)
        loc = self.driver.find_element(By.XPATH, "//input[@id='200']")
        self.a.move_to_element(loc).send_keys("Hyderabad").click().perform()
        time.sleep(4)

        # time.sleep(5)
        f = self.driver.find_element(By.XPATH, "(//input[@type='text'])[6]")
        self.a.move_to_element(f).click().send_keys("Hyderabad").click().perform()
        time.sleep(5)

        self.driver.execute_script("window.scrollBy(0,200)")
        r = self.driver.find_element(By.XPATH, "//input[contains(@data-validation-msg,'Please enter valid email')]")
        self.a.move_to_element(r).click().send_keys("pavanb1997@gmail.com").click().perform()
        time.sleep(5)
        f2 = self.driver.find_element(By.XPATH, "(//input[@type='text'])[7]")
        self.a.move_to_element(f2).click().send_keys("Telangana").click().perform()
        time.sleep(5)
        p = self.driver.find_element(By.XPATH, "(//input[@type='number'])[2]")
        self.a.move_to_element(p).click().send_keys("7095626420").click().perform()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "(//span[@class='checkmark-radio'])[2]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//input[@value="Proceed to pay"]').click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, '//div[@class="expand-icon"]').click()
        time.sleep(10)
        print(self.driver.find_element(By.XPATH, '(//div[@class="fareBreakupComp"])[2]').text)
        time.sleep(5)
        d = self.driver.find_elements(By.XPATH, '//div[@class="breakup slide-down"]')
        for i in d:
            print(i.text)

        c =self.driver.find_element(By.XPATH,"(//div[@class='fareBreakupComp ']/div)[2]").text
        r = (c.split(" "))
        x = r[1].replace(",", "")
        conert = int(x)
        print("Fair price of the ticket",x)
        k = self.driver.find_element(By.XPATH,'(//div[@class="fareBreakupComp "]/div)[4]').text
        f = k.split(" ")
        f2 = (f[2])
        c = re.search("\d*", f2).group()
        c2 = int(c)
        print("Gst on the ticket",c2)
        k2= self.driver.find_element(By.XPATH,'//div[@class="fareBreakupComp offer"]/div[2]').text
        f5 = k2.split(" ")
        f3 = (f5[2])
        c5 = re.search("\d*", f3).group()
        c3 = int(c5)
        print("Offer price in redbus",c3)
        print("The price difference between before payment and in payment page is :-", conert+c2-c3- original_price )

ss = Redbus()
ss.Create_Account()