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
class fide():
    def __int__(self):
        driver = webdriver.Chrome()
        self.driver = driver
        self.a = ActionChains(driver)
        self.date =date.today()

    def fide_login(self):
        self.__int__()
        self.driver.get("https://www.fide.com/")
        self.driver.find_element(By.XPATH, "//a[@class='nav-link'][normalize-space()='Ratings']").click()

    def indain_champs(self):
        self.fide_login()
        global row_data
        temp = []
        row_data = []
        c = self.driver.find_elements(By.XPATH, '//table/tbody/tr[" + str(index + 1) + "]')
        for index in range(len(c)):
            cell_data = self.driver.find_elements(By.XPATH, "//table/tbody/tr[" + str(index + 1) + "]/td")
            for data in cell_data:
                temp.append(data.text)
            if "IND" in temp:
                row_data.append(temp)
            temp = []
        # print(row_data)
    def ranks_id(self):
        self.indain_champs()
        self.driver.get("https://ratings.fide.com/")
        global ids
        global names
        global ranks
        ranks = []
        name = []
        for i in range(len(row_data)):
            name.append(row_data[i][1])
            ranks.append(row_data[i][0])
        # print(ranks,name)
        names = []
        ids = []
        for i in ranks:
            time.sleep(2)
            if self.driver.find_element(By.XPATH, "//table/tbody/tr[" + str(i) + "]/td[1]").text == i:
                self.driver.find_element(By.XPATH, "//table/tbody/tr[" + str(i) + "]/td[2]/a").click()
                names.append(self.driver.title)
                id = self.driver.find_element(By.XPATH,'//div[@class="col-lg-12 profile-top-info"]/div[1]/div[3]/div[2]').text
                ids.append(id)
                self.driver.get("https://ratings.fide.com/")
                time.sleep(2)
        print("id" ,"name ","rank")
        for i in range(len(ids)):
            print(ids[i], names[i], ranks[i])


    def current_tournments(self):
        self.ranks_id()
        dt = self.date.today()
        print("Today's dt:", dt)
        date1 = str(dt).split("-")
        print(date1)
        self.driver.get("https://ratings.fide.com/rated_tournaments.phtml")
        time.sleep(5)
        total_list = self.driver.find_elements(By.XPATH, "//table//tbody/tr")
        print("All tournaments:", len(total_list))
        crt_trs = []
        for r in range(2, len(total_list)):
            tr = self.driver.find_element(By.XPATH, "//table//tbody/tr[" + str(r) + "]/td[2]").text
            dt = self.driver.find_element(By.XPATH, "//table//tbody/tr[" + str(r) + "]/td[5]").text
            ct = self.driver.find_element(By.XPATH, "//table//tbody/tr[" + str(r) + "]/td[3]").text
            r=dt.split("-")
        if (int(dt.split("-")[2]) >= int(date1[2])) and \
                (int(dt.split("-")[1]) >= int(date1[1])) and \
                (int(dt.split("-")[0]) >= int(date1[0])):


                crt_trs.append({"Tournament Name": tr, "Place": ct, "Start Date": dt})

        print("total current tournaments:", len(crt_trs))

        for i in crt_trs:
            print(i)
        return self.driver
ss = fide()
# ss.ranks_id()
ss.current_tournments()