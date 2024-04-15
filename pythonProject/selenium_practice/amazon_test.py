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




driver.implicitly_wait(20)

driver.get("https://www.amazon.in/ref=nav_logo")
driver.maximize_window()
# move = driver.find_element(By.XPATH,'//span[@id="nav-link-accountList-nav-line-1"]')
# a.move_to_element(move).perform()
# move2 =driver.find_element(By.XPATH,'//span[@class="nav-action-inner"]')
# a.move_to_element(move2).click().perform()
# driver.find_element(By.XPATH,'//input[@type="email"]').send_keys("7095626420")
# driver.find_element(By.ID,"continue").click()
#
# driver.find_element(By.XPATH,'//input[@type="password"]').send_keys("pavan123")
# driver.find_element(By.ID,'signInSubmit').click()
#
# driver.find_element(By.ID,'twotabsearchtextbox').send_keys("TV")
# driver.find_element(By.XPATH,'//input[@type="submit"]').click()
# r = []
# for i in range(3,7):
#     driver.find_element(By.XPATH,'//div[@data-index= "'+str(i)+'"]//descendant::a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]').click()
#     parent_window = driver.current_window_handle
#
#     windows = driver.window_handles
#     for child in windows :
#         if parent_window != child :
#             driver.switch_to.window(child)
#             c = driver.find_element(By.XPATH,'//span[@class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"]//span[@class="a-price-whole"]').text
#             r.append(c)
#             time.sleep(5)
#             driver.find_element(By.XPATH, '//input[@id="add-to-cart-button"]').click()
#             time.sleep(5)
#             driver.close()
#             # driver.find_element(By.XPATH,'//a[@id="attach-close_sideSheet-link"]').click()
#             driver.switch_to.window(parent_window)
# print(r)
# v  =[]
# for i in r:
#     c=i.replace(",","")
#     v.append(int(c))
# total = "sum of all the prodects",sum(v)
# print(total)
# time.sleep(5)
# driver.find_element(By.ID,"nav-cart-count").click()
# time.sleep(5)
# c = driver.find_element(By.XPATH,"(//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap']//parent::span//child::span)[1]").text
#
# s =c.lstrip()
# p =s.replace(",","")
# vv =p.split(".")
# print(vv[0],type(vv[0]))
# print(total[1],type(total[1]))
# if vv[0] == str(total[1]) :
#     print("both are same")
# else:
#     print("not same ")

