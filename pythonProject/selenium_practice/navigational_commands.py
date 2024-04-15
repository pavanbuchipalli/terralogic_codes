from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
driver = webdriver.Chrome(r'C:\Users\PavanB-3247\PycharmProjects\pythonProject\driver\chromedriver.exe')

driver.get("https://www.snapdeal.com/?utm_source=admitad_846&utm_campaign=14be7d76511158cda7cfa2951943f770&utm_content=admitad_846&publisher_id=586854")

driver.get("https://www.primevideo.com/offers/nonprimehomepage/ref=dvm_pds_amz_in_as_s_gm_159_mkw_sRumWk2Nj-dc?gclid=CjwKCAjw0N6hBhAUEiwAXab-TZiqUzUs_JfDsj7Iu7CqkEGoDDizQNvJ4p62ajxEI9gxPQmAE2LhABoCrk8QAvD_BwE&mrntrk=pcrid_610141119732_slid__pgrid_84577172328_pgeo_9062006_x__adext__ptid_kwd-303629226711")

cc= driver.title
print(cc)




driver.back()
ff =driver.title
print(ff)


driver.forward()
rr =driver.title
print(rr)



driver.refresh()

driver.close()