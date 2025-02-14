import pytest
from selenium import webdriver

@pytest.fixtue()
def general_settings ():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.quit()
