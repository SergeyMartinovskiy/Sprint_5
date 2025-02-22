from Locators import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from my_data import *


class TestOutAccount:
    def test_log_out_account(self,general_settings):
        general_settings.find_element(*Locator.button_personal_account).click()
        general_settings.find_element(*Locator.email_field).send_keys(email)
        general_settings.find_element(*Locator.password_field).send_keys(password)
        general_settings.find_element(*Locator.button_enter).click()
        general_settings.find_element(*Locator.button_personal_account).click()
        WebDriverWait(general_settings, 10).until(expected_conditions.visibility_of_element_located(Locator.button_exit_from_account))
        general_settings.find_element(*Locator.button_exit_from_account).click()
        WebDriverWait(general_settings, 10).until(expected_conditions.visibility_of_element_located(Locator.text_enter_in_account))
        checking_text_enter = general_settings.find_element(*Locator.text_enter_in_account).text
        assert checking_text_enter == "Вход"



