import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import ASSIGNEMT2.config

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(ASSIGNEMT2.config.Config.gmail_url)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()