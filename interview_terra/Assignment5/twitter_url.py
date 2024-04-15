import time

url= """Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers for tesla related news,
 https://twitter.com/teslarati https://twitter.com/dummy_tesla https://twiter.com/dummy_2_tesla"""
s = url.split()
urls =[]

for i in s:
    if "https" in i:
        if "," in i:
            j = (i.split(','))[0]
            urls.append(j)
        else:
            urls.append(i)
print("Total urls in the given sting ",urls)
count  = 0
s = []
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome()
driver = driver
a = ActionChains(driver)
for i in urls:
    driver.get(i)
    time.sleep(8)
    c = driver.title
    if c == "Privacy error":
        count = count
    else:
        s.append(c)
        count += 1

print("The total number of valid url is {} ".format(count))
print(s)