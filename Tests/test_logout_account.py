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
        general_settings.find_element(*Locator.button_exit_from_account).click()
        checking_text_enter = general_settings.find_element(*Locator.text_enter_in_account).text
        WebDriverWait(general_settings, 3).until(expected_conditions.element_to_be_clickable(checking_text_enter))
        assert checking_text_enter == 'Вход'




