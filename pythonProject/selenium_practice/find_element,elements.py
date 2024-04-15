from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
driver = webdriver.Chrome(r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')
driver.implicitly_wait(10)
a = ActionChains(driver)

#find element_by Xpath
class elements():
    def find_element(self):
        driver.get("https://demo.nopcommerce.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH,("//div[@class='master-wrapper-page']//input[@type='text']")).send_keys("pavan")
        time.sleep(3)   #finding single  element in the webpage
        driver.close()
    def find_element2(self):
        driver.get("https://demo.nopcommerce.com/")
        driver.maximize_window()
        ele = driver.find_element(By.XPATH,"//div[@class='footer']//a").text
        print(ele)  #xpath is written for multiple elements but fin element find only one which it encounters first
        time.sleep(3)
        driver.close()

    def nosuchelement(self):
        driver.get("https://demo.nopcommerce.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, ("//div[@class='master-wrapper-page']//inut[@type='text']")).send_keys("pavan")
        time.sleep(3) #trows error when we gave wrong xpath or invalid xpath (no such element found)
        driver.close()

# ss = elements()
# ss.nosuchelement()


# find elements by Xpath
class elemens():
    def single_element(self):
        driver.get("https://demo.nopcommerce.com/")
        driver.maximize_window()
        ele = driver.find_elements(By.XPATH, ("//div[@class='master-wrapper-page']//input[@type='text']"))
        print(len(ele))
        time.sleep(3)  # finding single  element in the webpage
        driver.close()

    def multiple_elements(self):
        driver.get("https://demo.nopcommerce.com/")
        driver.maximize_window()
        ele = driver.find_elements( By.XPATH, "//div[@class='footer']//a")
        print(len(ele))
        print(ele[0].text)
        time.sleep(3)  # finding multiple  element in the webpage
        driver.close()

rr = elemens()
rr.multiple_elements()
