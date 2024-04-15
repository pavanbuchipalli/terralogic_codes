import logging

from ASSIGNEMT2.Library.selnium_wapper import Seleniumwapper
from selenium.webdriver.common.by import By



class Gmail(Seleniumwapper):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, value):
        email = ((By.ID, 'identifierId'))
        self.enter_element(email,value)

    def click_next(self):
        next = ((By.XPATH, '//span[text()="Next"]'))
        self.click_element(next)

    def enter_password(self, value):
        password = ((By.XPATH, '//input[@name="Passwd"]'))
        self.enter_element(password,value)
    def click_on_sent_button(self):
        sent_mail =((By.XPATH, "//div[@class='TN bzz aHS-bnu']"))
        self.sent_mails(sent_mail)

    def sent_count(self):
        sent_mails =((By.XPATH, '(//span[@class="ts"])[6]'))
        self.take_data_of_sent_mails(sent_mails)

    def settings_logo(self):
        logo = ((By.XPATH,'//a[@class="FH"]'))
        self.click_element(logo)

    def full_setting(self):
        full =((By.XPATH,"//button[text()='See all settings']"))
        self.all_settings(full)

    def reply_click_button(self):
        reply=((By.XPATH,'//input[@id=":84"]'))
        self.click_element(reply)

    def save_changes(self):
        save =((By.XPATH,'//button[@id=":6y"]'))
        self.click_element(save)
        logging.info("successful")

