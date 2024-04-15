# Import date class from datetime module
from datetime import date
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

# driver.get("https://ratings.fide.com/rated_tournaments.phtml")
# players_details= []
# players_list=driver.find_elements(By.XPATH, '//table/tbody/tr[" + str(index + 1) + "]')
# print("Total count of players",len(players_list))
# print("list_of_indian_players\n")
# for total in players_list:
#     players_details.append(total.text)
# for ind_playes in players_details:
#     if "IND" in ind_playes:
#         print(ind_playes)


# c =driver.find_elements(By.XPATH, "//table/tbody/tr")
# row_data=[]
# temp=[]
# c = driver.find_elements(By.XPATH, '//table/tbody/tr[" + str(index + 1) + "]')
# for index in range(len(c)):
#     cell_data=driver.find_elements(By.XPATH,"//div[@id='top_rating_div']//descendant::th//following::tr[" + str(index + 1) + "]/td")
#     for data in cell_data:
#         temp.append(data.text)
#     if "IND" in temp:
#         row_data.append(temp)
#     temp=[]
# print(row_data)
# r =[]
# n = []
# for i in range(len(row_data)):
#     n.append(row_data[i][1])
#     r.append(row_data[i][0])
# print(r,n)
# # cell_data=self.driver.find_elements(By.XPATH,"//div[@id='top_rating_div']//descendant::th//following::tr[" + str(index + 1) + "]/td")//table/tbody/tr[9]/td[2]/a
# names= []
# ids = []
# for i in r:
#     if driver.find_element(By.XPATH,"//table/tbody/tr[" + str(i) + "]/td[1]").text == i:
#         driver.find_element(By.XPATH,"//table/tbody/tr[" + str(i) + "]/td[2]/a").click()
#         names.append(driver.title)
#         id =driver.find_element(By.XPATH,'//div[@class="col-lg-12 profile-top-info"]/div[1]/div[3]/div[2]').text
#         ids.append(id)
#         driver.get("https://ratings.fide.com/")
#         time.sleep(5)
#         print(ids,names)
# date =date.today()
# print(str(date))
# print(type(date))
# t =[]
# c = driver.find_elements(By.XPATH,'//table/tbody/tr[@role="row"]')
# for i in c:
#     t.append(i.text)
# # print(t)
for i in range(2,1001):
    date_list= driver.find_elements(By.XPATH,'//table//tr/td[5]')

#
# date = date.today()
# print(date, type(date))
# date1 = str(date).split("-")
# print(date1, type(date1))
# for i in date1:
#     if int(i) >=
# for i in range(len(t)):
#     if driver.find_element(By.XPATH, '//table/tbody/tr[@role="row"][" + str(i) + "]/td[5]').text == date:
#         print(driver.find_element(By.XPATH, '//table/tbody/tr[@role="row"][" + str(i) + "]/td[5]'))
#     else:
#         print("no match")
































# l=[]
# # for i in range(len(c)):
# time.sleep(4)
#
# w=driver.find_element(By.XPATH,'//table/tbody/tr[" + str(10) + "]').text
# l.append(w)
# print(l)
# for i in range(len(r)):
#     if r[i] in row_data[i]:
#         driver.find_elements(By.XPATH,'//table/tbody/tr[" + str(j) /td[2]').click
#     time.sleep(10)

 # cell_data=self.driver.find_elements(By.XPATH,"//div[@id='top_rating_div']//descendant::th//following::tr[" + str(index + 1) + "]/td")
 #            for data in cell_data:
 #                temp.append(data.text)
 #            if "IND" in temp:
 #                row_data.append(temp)
 #            temp=[]
 #        print(row_data)
 #        print(row_data[0][1])
date = date.today()
print("Today's date:", date)
date1 = str(date).split("-")
print(date1)

driver.get("https://ratings.fide.com/rated_tournaments.phtml")
time.sleep(5)
tr_list = driver.find_elements(By.XPATH, "//table//tbody/tr")
print("total tournaments:", len(tr_list))
crt_trs = []
# r=[]
# for i in range(2,1000):
#     c = driver.find_elements(By.XPATH,'//table/tbody/tr[" + str(i) + "]/td[5]')
#     for j in c:
#         j.split("-")
#         r.append(j)
# print(r)

# print(c.split("-"))

for r in range(2, len(tr_list) + 1):
    date = driver.find_element(By.XPATH, "//table//tbody/tr[" + str(r) + "]/td[5]").text
    Tournment = driver.find_element(By.XPATH, "//table//tbody/tr[" + str(r) + "]/td[2]").text
    city = driver.find_element(By.XPATH, "//table//tbody/tr[" + str(r) + "]/td[3]").text
    if (int(date.split("-")[2]) >= int(date1[2])) and \
            (int(date.split("-")[1]) >= int(date1[1])) and \
            (int(date.split("-")[0]) >= int(date1[0])):
        crt_trs.append({"Tournament Name": name, "Place": city, "Start Date": date})
print("total current tournaments:", len(crt_trs))

for i in crt_trs:
    print(i)

