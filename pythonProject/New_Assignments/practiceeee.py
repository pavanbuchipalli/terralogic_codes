from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to the ChromeDriver executable
# chrome_driver_path = r'C:/Users/PavanB-3247/PycharmProjects/pythonProject/driver/chromedriver.exe'

# Creating a Service object
# service = Service(chrome_driver_path)

# Creating a WebDriver instance
driver = webdriver.Chrome()

# Rest of your Selenium code goes here


# ch = Options()
# ch.add_argument("--disable-notifications")
#
#
# driver = webdriver.Chrome(r'C:/Users/PavanB-3247/PycharmProjects/pythonProject/driver')
# driver = driver
a = ActionChains(driver)
#
#
driver.get("https://www.redbus.in/bus-tickets/bangalore-to-hyderabad?fromCityName=Bangalore&fromCityId=122&toCityName=Hyderabad&toCityId=124&onward=15-May-2023&srcCountry=IND&destCountry=IND&opId=0&busType=Any")
#
#
#
time.sleep(2)
#
#
driver.find_element(By.XPATH,"//div[text()='Lower Deck']//following-sibling::*")
# # r= c.get_attribute("class")
# e = driver.find_element(By.XPATH,"//canvas[@data-type='lower']")
# locatio =e.location
# sicz= e.size
# w, h = sicz['width'], sicz['height']
# print(locatio)
# print(sicz)
# a.move_to_element_with_offset(e,39,39).click().perform()
# time.sleep(5)
# a.move_to_element_with_offset(e,38,38).click().perform()
# time.sleep(4)

# for i in range(1,200):
#     # for j in range(1,200):
#
#     a.move_to_element_with_offset(e,0+i,0+i).click().perform()
#     time.sleep(3)
#     print(i)
# a.move_to_element_with_offset(e,100,110).click().perform()
# time.sleep(3)
# a.move_to_element_with_offset(e,120,120).click().perform()
# time.sleep(3)
# a.move_to_element_with_offset(e,130,130).click().perform()
# time.sleep(3)
# a.move_to_element_with_offset(e,140,140).click().perform()
# time.sleep(3)
# a.move_to_element_with_offset(e,150,150).click().perform()
# time.sleep(3)
# a.move_to_element_with_offset(e,160,170).click().perform()
# time.sleep(4)
# a.move_to_element_with_offset(e,170,190).click().perform()
# time.sleep(3)

# a.move_by_offset(100,100).click().perform()
# a.move_by_offset( 150, 100).click().perform()
# a.move_by_offset( 175, 100).click().perform()
# a.move_by_offset( 200, 100).click().perform()
# a.move_by_offset(100,150).click().perform()
# # a.move_by_offset(100,170).click().perform()
# # a.move_by_offset(100,200).click().perform()
# # a.move_by_offset(100,250).click().perform()

time.sleep(10)
