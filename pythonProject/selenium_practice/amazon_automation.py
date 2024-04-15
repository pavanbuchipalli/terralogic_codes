# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.action_chains import ActionChains
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.common.service import Service
# # from selenium.webdriver.support.wait import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time
# # import unittest
# #
# #
# #
# #
# # class amazon:
# #
# #     def __int__(self):
# #         driver = webdriver.Chrome(r"C://Users//PavanB-3247//Downloads//chrome-win64.zip")
# #         self.driver = driver
# #         self.a = ActionChains(driver)
# #
# #     def login_to_amazon(self):
# #         self.__int__()
# #         self.driver.get("https://www.amazon.in/ref=nav_logo")
# #         self.driver.maximize_window()
# #         move = self.driver.find_element(By.XPATH, '//span[@id="nav-link-accountList-nav-line-1"]')
# #         self.a.move_to_element(move).perform()
# #         move2 = self.driver.find_element(By.XPATH, '//span[@class="nav-action-inner"]')
# #         self.a.move_to_element(move2).click().perform()
# #         self.driver.find_element(By.XPATH, '//input[@type="email"]').send_keys("7095626420")
# #         self.driver.find_element(By.ID, "continue").click()
# #
# #         self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("Yugesh@05")
# #         self.driver.find_element(By.ID, 'signInSubmit').click()
# #
# #     def validations_of_title(self):
# #         self.login_to_amazon()
# #         time.sleep(5)
# #         original_title = self.driver.title
# #
# #         Expected_title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
# #         if original_title == Expected_title:
# #             print("We are in Desitination page")
# #
# #         else:
# #             print("We are not in the desination page")
# #
# #     def Sending_input_to_searchbox(self):
# #         self.login_to_amazon()
# #
# #         self.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("TV")
# #         self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()
# #
# #     def Selecting_Tvs_adding_to_cart(self):
# #         self.Sending_input_to_searchbox()
# #         price_of_Tvs = []
# #         for i in range(3, 7):
# #             self.driver.find_element(By.XPATH, '//div[@data-index= "' + str(i) + '"]//descendant::a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]').click()
# #             parent_window = self.driver.current_window_handle
# #
# #             windows = self.driver.window_handles
# #             for child in windows:
# #                 if parent_window != child:
# #                     self.driver.switch_to.window(child)
# #                     c = self.driver.find_element(By.XPATH,'//span[@class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"]//span[@class="a-price-whole"]').text
# #                     price_of_Tvs.append(c)
# #                     time.sleep(5)
# #                     self.driver.find_element(By.XPATH, '//input[@id="add-to-cart-button"]').click()
# #                     time.sleep(5)
# #                     self.driver.close()
# #
# #                     self.driver.switch_to.window(parent_window)
# #
# #         print("list_of_the_prices_of_Tvs",price_of_Tvs)
# #         global  total
# #         list_of_prices = []
# #         for i in price_of_Tvs:
# #             c = i.replace(",", "")
# #             list_of_prices.append(int(c))
# #         self.total = "sum of all the prodcts", sum(list_of_prices)
# #         print(self.total)
# #
# #     def subtotal_of_Tvs(self):
# #         global  subtotal_number
# #         self.Selecting_Tvs_adding_to_cart()
# #         self.driver.find_element(By.ID, "nav-cart-count").click()
# #         element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"(//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap']//parent::span//child::span)[1]")))
# #         subtotal = self.driver.find_element(By.XPATH,"(//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap']//parent::span//child::span)[1]").text
# #         self.subtotal_number = subtotal.lstrip().replace(",", "").split(".")
# #         print  ("Sub_total_in_the_cart=",self.subtotal_number[0])
# #
# #     def validation(self):
# #         self.total
# #         self.subtotal_number
# #         if  str(self.total[1]) == self.subtotal_number[0] :
# #             # print(self.total[1])
# #             # print(self.subtotal_number[0])
# #             print("Both the totals are same ")
# #         else:
# #             print("Both the totals not same")
# #
# #
# #
# # ss = amazon()
# # ss.subtotal_of_Tvs()
# # ss.validation()
# #
# import paramiko
#
# # Server information
# hostname = '192.168.250.102'
# port = 22  # Default SSH port
# username = 'terralogic'
#
# # Create an SSH client
# client = paramiko.SSHClient()
#
# # Automatically add the server's host key (this is insecure and should be avoided in production)
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# # Connect to the server
# try:
#     client.connect(hostname, port=port, username=username)
#
#     # Example: Run a command on the server (replace this with your specific actions)
#     stdin, stdout, stderr = client.exec_command('ls -l')
#
#     # Print the output of the command
#     print("Command Output:")
#     print(stdout.read().decode('utf-8'))
#
# finally:
#     # Close the connection
#     client.close()
# str="abcabcdafsweraumbrella"
# 	le = len(str)
# 	op = ""
# 	new = ""
# 	for i in range(len(str) - 1):
# 		if str[i] not in op :
# 			op = op + str[i]
# 			if i == len(str) - 1:
# 				if op > new:
#                     new = op
#
# 		else:
# 			if len(op) > new:
#                 new = op
# 			   op = str[i]
# 			else:
# 				op = str[i]
#
#
# 	print(op)