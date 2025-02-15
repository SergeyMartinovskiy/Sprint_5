import pytest
from selenium import webdriver

@pytest.fixture()
def general_settings ():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()
