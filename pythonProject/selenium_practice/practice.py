from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import copy
driver = webdriver.Chrome()

a = ActionChains(driver)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(5)
#
#
driver.find_element(By.NAME,"q").send_keys("Netflix")
a.send_keys(Keys.ENTER)
a.perform()
driver.find_element(By.XPATH,"//h3[text()='Netflix - Watch TV Shows Online, Watch Movies Online']").click()

driver.find_element(By.XPATH,"//a[text()='Sign In']").click()

driver.find_element(By.XPATH,"//input[@id='id_userLoginId']").send_keys("draj040327@gmail.com")

driver.find_element(By.XPATH,"//input[@id='id_password']").send_keys("Only@5people")
time.sleep(4)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
driver.find_element(By.XPATH,"(//div[@class='avatar-wrapper'])[1]").click()
time.sleep(2)

# # driver.find_element(By.XPATH,"//button[@class='searchTab']").click()
# # time.sleep(5)
#
# search = driver.find_element(By.XPATH, "//button[@aria-label='Search']")
# a.move_to_element(search).click().send_keys("Money Heist").click().perform()
# time.sleep(5)
# # time.sleep(20)
# # ele = driver.find_element(By.XPATH,"(//div[@class='boxart-size-16x9 boxart-container boxart-rounded'])[1]")
# #
# # a.move_to_element(ele).click().perform()
# # # time.sleep(5)
# # # driver.execute_script("window.scrollTo(0, 600)")
# # # time.sleep(5)
# # # driver.find_element(By.XPATH,"//div[@class='episodeSelector-dropdown']//div[@class='ltr-1bbjknu']/button").click()
# # # time.sleep(3)
# # # ele2 = driver.find_element(By.XPATH,"//li[text()='See All Episodes']")
# # # a.move_to_element(ele2).click().perform()
# # # time.sleep(10)
# # # list_of_time = [ ]
# # # total_duration = driver.find_elements(By.XPATH,"//div[@class='titleCardList-title']//span[@class='duration ellipsized']")
# # # for single_episode in total_duration:
# # #     convert= (str(single_episode.text)).replace("m","")
# # #     list_of_time.append(int(convert))
# # # print("The Total Duration of the Money heist Web Series is :- ",sum(list_of_time),"Mins")
# # #
#
#
#
#
#
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.service import Service
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import copy
# driver = webdriver.Chrome()
#
# a = ActionChains(driver)
#
#
# #
# #
# # driver.get("https://wynk.in/music/search")
# # time.sleep(20)
# # r=[]
# # SCROLL_PAUSE_TIME = 2
# #
# # # Get scroll height
# # last_height = driver.execute_script("return document.body.scrollHeight")
# #
# # while True:
# #     # Scroll down to bottom
# #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # flag = driver.find_element(By.XPATH, "//body")
# # print(flag.text)
#     # flag.send_keys(Keys.SPACE)
# #     # Wait to load page
# #     time.sleep(SCROLL_PAUSE_TIME)
# #
# #     # Calculate new scroll height and compare with last scroll height
# #     new_height = driver.execute_script("return document.body.scrollHeight")
# #     if new_height == last_height:
# #         break
# #     last_height = new_height
#
# # print("List Of Telugu Songs Start with R is :-")
# # c = last_height = driver.execute_script("return document.body.scrollHeight")
# # print(c)
# # while True:
# #     body = driver.find_element(By.XPATH,'/html/body')
# #     # body.click()
# #     ActionChains(driver).send_keys(Keys.DOWN).perform()
# #     # flag = driver.find_element(By.XPATH, "//body")
# #     # flag.send_keys(Keys.SPACE)
# #     time.sleep(4)
# #     p = driver.find_elements(By.XPATH,"//div[@class='zapSearch_zapSearchList__TvGT1']//div/h5")
# #
# #     for i in p:
# #         print(i.text)
# #         r.append(c)
# #     #
# #     # for i in r:
# #     #     if i.startswith("R"):
# #     #
# #     #         print(i)
# #     f = new_height = driver.execute_script("return document.body.scrollHeight")
# #     print(f)
# #     # if new_height == last_height:
# #     #     break
# #     # last_height = new_height
# #
# # #     if
#
#
#
#
# # driver.get("https://www.swiggy.com/restaurants/chaayos-chai-snacks-relax-5th-block-koramangala-bangalore-263485")
# # time.sleep(30)
# # c = driver.find_elements(By.XPATH,"(//div[@class='main_container__3QMrw'])[1]//div[text()='ADD']")
# # p =[]
# # for i in c:
# #     driver.execute_script("window.scrollBy(0,200)")
# #     time.sleep(3)
# #     i.click()
# #
# #     time.sleep(4)
# #     try:
# #
# #         driver.find_element(By.XPATH, "//span[text()='Continue']").click()
# #         time.sleep(3)
# #         driver.find_element(By.XPATH, "//span[@class='_38xdN']").click()
# #         c =driver.find_element(By.XPATH,"//div//span[@class='_3RJsr']").text
# #         r = re.search('[0-9]*', c).group()
# #         p.append(int(r))
# #         time.sleep(3)
# #
# #     except :
# #         driver.find_element(By.XPATH,"//span[@class='_38xdN']").click()
# #         c = driver.find_element(By.XPATH, "//div//span[@class='_3RJsr']").text
# #         r = re.search('[0-9]*', c).group()
# #         p.append(int(r))
# #         time.sleep(3)
# #     if len(p) == 4 :
# #         break
# #
# # print(p)
# #
# # import re
# # c = []
# # import math
# # p = ['129.00', '159.00', '169.00', '179.00']
# # for i in p:
# #     i.split(".")
# #     print(i,type(i))
# #     r =re.search('[0-9]*', i).group()
# #     c.append(int(r))
# # print(sum(c))
# # driver.get("https://www.swiggy.com/checkout")
# # time.sleep(40)
# # driver.find_element(By.XPATH,"(//div[@class='_33KRy'])[1]").click()
# # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# #
# # time.sleep(10)
# # su = driver.find_element(By.XPATH,"//div[@class='_3rlIu']/div[2]").text
# # print(su)
#
# ele = driver.find_element(By.ID,"txtSource")
# a.move_to_element(ele).click().send_keys("Bangalore").send_keys(Keys.ENTER)
# # a.send_keys(Keys.ENTER)
# # a.perform()
# # time.sleep(5)
# # ele = driver.find_element(By.ID,"txtDestination")
# # a.move_to_element(ele).click().send_keys("Hyderabad").click().perform()
# # time.sleep(1)
# # ele2 =driver.find_element(By.XPATH,"//input[@id='txtOnwardCalendar']")
# # a.move_to_element(ele2).click().perform()
# #
# # ele2 = driver.find_element(By.XPATH,"(//div[@id='rb-calmiddle'])[1]/ul[2]/li[14]")
# # a.move_to_element(ele2).click().perform()
# # time.sleep(3)
# # driver.find_element(By.XPATH,"//button[@class='D120_search_btn searchBuses']").click()
# # time.sleep(10)
# #
# #
# # c = driver.find_element(By.XPATH,"//span[@class='f-bold busFound']").text
# # print(c)
# #
# #
# #
# # driver.execute_script("window.scrollBy(0,250)")
# # time.sleep(10)
# #
# # driver.find_element(By.XPATH,"(//div[@class='clearfix bus-item'])[1]/div[2]/div[1]").click()
# # time.sleep(10)
# # r = driver.find_element(By.XPATH,"(//div[@class='clearfix row-one'])[1]/div[6]//span").text
# # print(r)
# # s =driver.find_element(By.XPATH,"(//div[@class='clearfix row-one'])[1]/div[7]//div[1]").text
# # print(s)
# # ch = Options()
# # ch.add_argument("--disable-notifications")
# # driver = webdriver.Chrome(options=ch)
# #
# # a = ActionChains(driver)
# #
# # driver.get("https://www.redbus.in/")
# # driver.maximize_window()
# # time.sleep(30)
import requests

def test_create_resource():
    url = "https://api.example.com/resource"
    data = {"key": "value"}
    response = requests.post(url, json=data)
    assert response.status_code == 201

def test_read_resource():
    url = "https://api.example.com/resource/1"
    response = requests.get(url)
    assert response.status_code == 200
    assert "key" in response.json()

# Add similar test cases for update and delete operations
