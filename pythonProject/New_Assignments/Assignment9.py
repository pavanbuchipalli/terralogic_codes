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
# self.driver = webdriver.Chrome(options=ch)
#
# a = ActionChains(self.driver)
class Redbus():

        def url(self):
            self.driver = webdriver.Chrome()
            self.driver = self.driver
            self.driver = webdriver.Chrome(options=ch)
            self.a = ActionChains(self.driver)

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
            time.sleep(3)
            self.driver = webdriver.Chrome()
            self.driver = self.driver
            self.a = ActionChains(self.driver)

            self.driver.get("https://www.redbus.in/")
            time.sleep(60)
            ele = self.driver.find_element(By.ID,"src")
            self.a.move_to_element(ele).click().send_keys("Bangalore").send_keys(Keys.ENTER)
            time.sleep(5)
            ele = self.driver.find_element(By.ID,"dest")
            self.a.move_to_element(ele).click().send_keys("Hyderabad").click().perform()
            time.sleep(1)
            ele2 =self.driver.find_element(By.ID,"onward_cal")
            self.a.move_to_element(ele2).click().perform()
            ele2 = self.driver.find_element(By.XPATH,"(//table/tbody/tr[4]/td[7]")
            self.a.move_to_element(ele2).click().perform()
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//button[text()='Search Buses']").click()
            time.sleep(10)


        def total_buses(self):
            self.route()
            time.sleep(5)
            aa = self.driver.find_element(By.XPATH,"//i[@class='icon icon-close']")
            self.a.move_to_element(aa).click().perform()
            c = self.driver.find_element(By.XPATH,"//span[@class='f-bold busFound']").text
            print(c)

        def seat_and_price(self):
            self.total_buses()
            self.driver.execute_script("window.scrollBy(0,250)")
            time.sleep(10)

            self.driver.find_element(By.XPATH, "(//div[@class='clearfix bus-item'])[1]/div[2]/div[1]").click()
            time.sleep(10)
            for i in range(2,6):
                r = self.driver.find_element(By.XPATH, "(//ul[@class='clearfix multiFare'/li["+str(i)+"]").text
                print(r)
            s = self.driver.find_element(By.XPATH, "(//div[@class='clearfix row-one'])[1]/div[7]//div[1]").text
            print(s)

ss =Redbus()
ss.url()



# driver.get("https://www.redbus.in/")
# driver.maximize_window()
# time.sleep(1)
# # part1
# c=driver.find_element(By.XPATH,"(//i[@class='icon icon-down D121_icon_down'])[1]").click()
# a.move_to_element(c).click().perform()
# time.sleep(4)
# ele = driver.find_element(By.ID,"src")
# a.move_to_element(ele).click().send_keys("Bangalore").click().perform()
# time.sleep(1)
# ele = driver.find_element(By.ID,"dest")
# a.move_to_element(ele).click().send_keys("Hyderabad").click().perform()
# time.sleep(1)
# driver.find_element(By.XPATH,"//label[@for='onward_cal']").click()
# ele2 = driver.find_element(By.XPATH,"//table//tr[4]/td[4]")
# a.move_to_element(ele2).click().perform()
# time.sleep(3)
# self.driver.find_element(By.XPATH,"//button[@id='search_btn']").click()
# time.sleep(10)







# driver.find_element(By.XPATH,"//button[@id='search_btn']").click()
# time.sleep(15)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(5)
# c = driver.find_elements(By.XPATH,"(//div[@scrollthreshold='1'])[2]/ul/div")
# time.sleep(10)
# print(len(c))
# driver.find_element(By.XPATH,"//ul[@class='dept-time dt-time-filter']/li")
# driver.find_element(By.XPATH,"//input[@id='dtBefore 6 am']").click()
# time.sleep(4)