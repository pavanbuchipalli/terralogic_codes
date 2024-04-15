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
a = ActionChains(driver)


#
# driver.get('https://www.swiggy.com/city/bangalore')
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.XPATH, "//div[text()='Setup your precise location']").click()
# time.sleep(10)
# driver.find_element(By.XPATH, "//input[@placeholder='Search for area, street name...']").send_keys("Koramangala")
# time.sleep(5)
#
# ele = driver.find_element(By.XPATH,'//*[text()="Locate me using GPS"]//ancestor::*[@class="style__Location-sc-zdau5c-1 fwrdJJ"]/following-sibling::div[1]')
# time.sleep(5)
# a.move_to_element(ele).click().perform()
# time.sleep(4)
# driver.execute_script("window.scrollTo(0, 1000)")
# time.sleep(10)
# # c = driver.find_element(By.XPATH,"//div[@class='BZR3j']").text
# # print("Total no of restarunts",c)
# # driver.execute_script("window.scrollTo(0, 1000)")
# time.sleep(30)
# # x= driver.find_elements(By.XPATH,'//div[@class="_3Ztcd"]/div[1]')
# # for i in x:
# #     print(i.text)
#
# # print("list of Restaurants")
# # for i in range(1, len(c)):
# #     time.sleep(3)
# #     s = "//div[@class='sc-iBdmCd hPntbc']/div[{}]//div//span[@class='sc-dmyDGi dpnlFb']".format(i)
# #     time.sleep(3)
# #
# #     print(driver.find_element(By.XPATH, s).text)
# # time.sleep(5)
