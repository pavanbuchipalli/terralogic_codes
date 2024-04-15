from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


import csv
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
mouse = ActionChains(driver)
driver.implicitly_wait(5)






# driver.get("https://seleniumbase.io/demo_page")
# time.sleep(5)
# title = driver.title
# if title == "Web Testing Page":
#
#     print("yes u r in right path ")
#
# else:
#     print("no ")

#
# driver.find_element(By.ID,('myTextInput')).send_keys("pavan")
# data =driver.find_element(By.ID,("myTextInput2"))
# data.clear()
# data.send_keys("office")
#
# driver.find_element(By.ID,"placeholderText").send_keys("neew")
#
# # dropdown1
# mouse_data = driver.find_element(By.ID,"mySelect")
# mouse.move_to_element(mouse_data).click().perform()
#
# dropdown_element = driver.find_element(By.ID,'mySelect')  # Replace "dropdown_id" with the actual ID of your dropdown
#
# dropdown = Select(dropdown_element)
#
#
# dropdown.select_by_visible_text("Set to 75%")
#
# #checkbox
# driver.find_element(By.XPATH,"//td/input[@id='checkBox2']").click()
#
# #link1
#
# driver.find_element(By.ID,"myLink1").click()
#
# #navigation
# driver.back()
#
# time.sleep(2)
#
# #dropdown2
# mouse_data2 = driver.find_element(By.ID,"myDropdown")
# mouse.move_to_element(mouse_data2).click().click().perform()
#
#
# mouse_data3 = driver.find_element(By.XPATH,"//a[@id='dropOption1']")
# mouse.move_to_element(mouse_data3).click().perform()
#
# #textarea
# driver.find_element(By.XPATH,"//textarea[@id='myTextarea']").send_keys("nothing")
# #button
# driver.find_element(By.XPATH,'//button[@id="myButton"]').click()
#
#
# #radio
# decision = driver.find_element(By.XPATH,"//input[@id='radioButton1']").is_selected()
# print(decision)
#
#
# time.sleep(5)


#

a =[1,2,4,5,7,8,33,44,11]
largest = 0
second_largest = 0
for i in a:
    if i > largest:
        second_largest = largest
        largest = i

    elif i > second_largest and i != largest:
        second_largest = i

print(second_largest)
