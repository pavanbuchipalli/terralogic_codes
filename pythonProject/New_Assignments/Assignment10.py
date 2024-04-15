from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
ch = Options()
ch.add_argument("--disable-notifications")
class Movie():

    def url(self):
        self.driver = webdriver.Chrome()
        self.driver = self.driver
        self.a = ActionChains(self.driver)
        self.driver.get("https://www.google.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def search(self):
        self.url()
        self.driver.find_element(By.NAME, "q").send_keys("PVR Cinemas")
        self.a.send_keys(Keys.ENTER)
        self.a.perform()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,150)")


    def login(self):
        self.search()
        self.driver.find_element(By.XPATH, "(//h3[text()='PVR Cinemas'])[1]").click()
        self.driver.find_element(By.XPATH, "//div[@class='nav-icon']").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Login with OTP')]").click()
        ele = self.driver.find_element(By.XPATH, "//input[@placeholder='Mobile']")
        self.a.move_to_element(ele).click().send_keys("7095626420").click().perform()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Login with OTP')]").click()
        ele2 = self.driver.find_element(By.XPATH, "//input[@placeholder='OTP']")
        self.a.move_to_element(ele2).click().perform()
        self.driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
        print("congratulations You are login to PVR Cinemas  -:", "\n", self.driver.title)
        self.driver.find_element(By.XPATH, '//div[@class="nav-icon icon-close"]').click()

    def count_of_shows(self):
        self.login()
        ele3 = self.driver.find_element(By.XPATH, "(//input[@role='searchbox'])[1]")
        self.a.move_to_element(ele3).click().send_keys("pvr Nexus").click().perform()
        ele4 = self.driver.find_element(By.XPATH, '//li[@role="option"]')
        self.a.move_to_element(ele4).click().perform()
        all_screens = self.driver.find_elements(By.XPATH, '//div[@class="m-cinema-listing"]//span[@class="extras"]')
        count = 1
        all_count = []
        for single in all_screens:
            time.sleep(3)
            single.click()
            time.sleep(4)
            shows = self.driver.find_elements(By.XPATH, '//div[@class="collpased active"]//span[@class="slot"]')
            print("shows in screen is {} ".format(count), len(shows))
            all_count.append(len(shows))
            count += 1

        print("total no of shows in all screens is ", sum(all_count))
        time.sleep(10)


    def Ticket_booking(self):
        self.count_of_shows()
        self.driver.find_element(By.XPATH, '(//span[@class="extras"])[1]').click()
        self.driver.find_element(By.XPATH,'(//div[@class="cinema-holder two-sec border-bottom fx col-mob ng-star-inserted"])[2]//li/span').click()

        self.driver.find_element(By.XPATH,'//button[@class="btn btn-primary-alt btn-gradient-dark btn-shadow text-uppercase full_width"]').click()
        price = self.driver.find_element(By.XPATH, '(//div/div[@class="ticket-value"])[1]').text
        print("price of the ticket is ", price)
        self.driver.find_element(By.XPATH, "//div[contains(text(),'APPLY OFFER')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Accept')]").click()
        seat_available = self.driver.find_elements(By.XPATH, '//span[contains(@class,"seat current")]')
        print("Total no of seats available is  ", len(seat_available))
        for i in seat_available:
            i.click()
            break
        self.driver.find_element(By.XPATH, '//i[@class="ion-arrow-right-c"]').click()

        ele = self.driver.find_element(By.XPATH, "(//button[contains(text(),'Cancel')])[2]")
        mywait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ele))
        ele.click()
        self.driver.find_element(By.XPATH, '//h5[contains(text(),"UPI")]').click()
        payment_price = self.driver.find_element(By.XPATH, "//span[@class='right lg ng-star-inserted']").text
        print("total price of ticket in payment page", payment_price)
        _price= payment_price.splitlines()
        payment_price = int(price[0])
        print("the difference between Actaul price and price in payment page is :-", payment_price - 240)
        time.sleep(10)




obj =Movie()
obj.Ticket_booking()



#use wait statement while login to enter the opt so that u wont get error at the end while code navigating to paymnet page

