import pytest
from selenium import webdriver
from URLS import Main_URL

@pytest.fixture()
def general_settings():
    driver = webdriver.Chrome()
    driver.get(Main_URL)
    yield driver
    driver.quit()
