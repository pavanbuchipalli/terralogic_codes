import time

from ASSIGNEMT2.pom.gmail_page import Gmail

def test_gmail_valid(setup):
    fp = Gmail(setup)
    email_value = "qq6630685@gmail.com"
    fp.enter_email(email_value)
    time.sleep(2)
    fp.click_next()
    time.sleep(5)
    password_value= "Yugesh@05"
    fp.enter_password(password_value)
    time.sleep(2)
    fp.click_next()
    time.sleep(3)
    fp.title_extraction()
    time.sleep(3)
















    # fp.click_on_sent_button()
    # time.sleep(3)
    # fp.sent_count()
    # time.sleep(3)
    # fp.settings_logo()
    # time.sleep(4)
    # fp.full_setting()
    # time.sleep(4)







