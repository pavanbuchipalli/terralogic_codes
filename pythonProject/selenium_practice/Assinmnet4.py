#
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
driver.implicitly_wait(10)

driver.get('https://olympics.com/en/')
time.sleep(3)
driver.maximize_window()
driver.find_element(By.XPATH, "//div[@id='onetrust-button-group']/button[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,'//span[text()="Sign In"]').click()
driver.find_element(By.ID,"email").send_keys("pavanb1997@gmail.com")
driver.find_element(By.XPATH,"//button[text()='Continue']").click()
time.sleep(3)
driver.find_element(By.ID,'password').send_keys("Yugesh@0512")
driver.find_element(By.XPATH,"//button[text()='Continue']").click()
time.sleep(3)

actual_title = "Olympics | Olympic Games, Medals, Results & Latest News"
Result_title = driver.title
if Result_title == actual_title :
    print("Yes you are in Tokyo 2020 ")

#task2

Olympic =driver.find_element(By.XPATH,"//section[@class='b2p-nav__extended']/ul/li[1]/a/span")
a.move_to_element(Olympic).perform()
driver.execute_script("window.scrollTo(0, 20)")
time.sleep(3)
Tokyo  =driver.find_element(By.XPATH,'//span[text()="Tokyo 2020"]')
time.sleep(5)
a.move_to_element(Tokyo).click().perform()
driver.find_element(By.XPATH,'//ul[@data-cy="nav-dropdown"]/li[3]/a').click()
time.sleep(5)
driver.execute_script("window.scrollTo(0, 1200)")
time.sleep(5)
driver.find_element(By.XPATH,'//p[text()="Badminton"]').click()
time.sleep(5)
#mens double
Mens_double = []
for i in range(1,4):

    c= driver.find_element(By.XPATH,"//div[@data-cy='award-card-" + str(i) + "-row-1']//div[@data-cy='two-athletes-award-card']").text
    Mens_double.append(c.splitlines())
print("Result of mens double :-",Mens_double)

#mens single
driver.find_element(By.XPATH,"//section[@data-row-id='award-row-2']//button[@class='styles__RowToggle-sc-282810-3 lejVUA']").click()
Mens_single = []
for i in range(1,4):

    c= driver.find_element(By.XPATH,"//div[@data-cy='award-card-"+ str(i) +"-row-2']/div[@data-cy='single-athlete-award-card']").text
    Mens_single.append(c.splitlines())
print("Result of mens single :-",Mens_single)

#mens mixed
Mens_mixed = []
driver.find_element(By.XPATH,"//section/div/button[@class='styles__CollapseButton-sc-54gbci-3 evOjtJ']").click()
time.sleep(5)
for i in range(1,4):

      c= driver.find_element(By.XPATH,"//div[@data-cy='award-card-" + str(i) +"-row-3']/div[@data-cy='two-athletes-award-card']").text
      Mens_mixed.append(c.splitlines())
print("Result of mens mixed :-",Mens_mixed)



driver.get("https://olympics.com/en/olympic-games/tokyo-2020/results/badminton")
time.sleep(4)
women_double = []
driver.find_element(By.XPATH, "//section[@data-row-id='award-row-4']/div[1]/button").click()
time.sleep(5)
for i in range(1, 4):
    c = driver.find_element(By.XPATH, "//div[@data-cy='award-card-" + str(i) + "-row-4']/div[@data-cy='two-athletes-award-card']").text
    women_double.append(c.splitlines())
print("Result of womens_double :-", women_double)

driver.get("https://olympics.com/en/olympic-games/tokyo-2020/results/badminton")
time.sleep(4)
womens_single= []
driver.find_element(By.XPATH,"//section[@data-row-id='award-row-5']/div[1]/button").click()
time.sleep(5)

for i in range(1,4):

      c= driver.find_element(By.XPATH,"//div[@data-cy='award-card-" + str(i) +"-row-5']/div[@data-cy='single-athlete-award-card']").text
      womens_single.append(c.splitlines())
print("Result of womens_single :-",womens_single)
