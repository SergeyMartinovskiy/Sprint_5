from Locators import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from my_data import *

class TestEnterLInLoginPage:
    def test_login_click_on_button_personal_account_in_mane_page (self, general_settings):
        general_settings.find_element(*Locator.button_enter_to_account).click()
        general_settings.find_element(*Locator.email_field).send_keys(email)
        general_settings.find_element(*Locator.password_field).send_keys(password)
        general_settings.find_element(*Locator.button_enter).click()
        checking_text_main_page = general_settings.find_element(*Locator.text_in_main_page).text
        WebDriverWait(general_settings, 3).until(expected_conditions.element_to_be_clickable(checking_text_main_page))
        assert checking_text_main_page == 'Оформите заказ'

    def test_login_through_button_personal_account (self, general_settings):
        general_settings.find_element(*Locator.button_personal_account).click()
        general_settings.find_element(*Locator.email_field).send_keys(email)
        general_settings.find_element(*Locator.password_field).send_keys(password)
        general_settings.find_element(*Locator.button_enter).click()
        checking_text_main_page = general_settings.find_element(*Locator.text_in_main_page).text
        WebDriverWait(general_settings, 3).until(expected_conditions.element_to_be_clickable(checking_text_main_page))
        assert checking_text_main_page == 'Оформите заказ'

    def test_login_through_button_registration (self, general_settings):
        general_settings.find_element(*Locator.button_personal_account).click()
        general_settings.find_element(*Locator.sign_registration).click()
        general_settings.find_element(*Locator.name_field).send_keys(user_name)
        general_settings.find_element(*Locator.email_field).send_keys(email)
        general_settings.find_element(*Locator.password_field).send_keys(password)
        general_settings.find_element(*Locator.button_registration).click()
        checking_text_main_page = general_settings.find_element(*Locator.text_in_main_page).text
        WebDriverWait(general_settings, 3).until(expected_conditions.element_to_be_clickable(checking_text_main_page))
        assert checking_text_main_page == 'Оформите заказ'


