from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
a = ActionChains(driver)

class iframe():
    def frame_i(self):
        driver.get("https://demo.automationtesting.in/Frames.html")
        driver.maximize_window()
        driver.switch_to.frame("packageListFrame")
        driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
        driver.switch_to.default_content()
        driver.switch_to.frame("packageFrame")
        driver.find_element(By.LINK_TEXT, "WebDriver").click()
        driver.switch_to.default_content()
        driver.switch_to.frame("classFrame")
        driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()


    def nested_frame(self):
        driver.get("https://demo.automationtesting.in/Frames.html")
        driver.maximize_window()

        driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
        time.sleep(5)
        outer_frame = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
        driver.switch_to.frame(outer_frame)

        inner_frame= driver.find_element(By.XPATH,"//iframe[normalize-space()='<p>Your browser does not support iframes.</p>']")
        driver.switch_to.frame(inner_frame)
        driver.find_element(By.XPATH,'//input[@type="text"][1]').send_keys("Welcome")



ss =iframe()
# ss.frame_i()
ss.nested_frame()
