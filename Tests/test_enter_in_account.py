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
        WebDriverWait(general_settings, 3).until(expected_conditions.visibility_of_element_located(Locator.text_in_main_page))
        checking_text_main_page = general_settings.find_element(*Locator.text_in_main_page).text
        assert checking_text_main_page == 'Оформить заказ'

    def test_login_through_button_personal_account (self, general_settings):
        general_settings.find_element(*Locator.button_personal_account).click()
        general_settings.find_element(*Locator.email_field).send_keys(email)
        general_settings.find_element(*Locator.password_field).send_keys(password)
        general_settings.find_element(*Locator.button_enter).click()
        WebDriverWait(general_settings, 3).until(expected_conditions.visibility_of_element_located(Locator.text_in_main_page))
        checking_text_main_page = general_settings.find_element(*Locator.text_in_main_page).text
        assert checking_text_main_page == 'Оформить заказ'

    def test_login_through_button_registration (self, general_settings):
        general_settings.find_element(*Locator.button_personal_account).click()
        general_settings.find_element(*Locator.sign_registration).click()
        general_settings.find_element(*Locator.name_field).send_keys(user_name)
        general_settings.find_element(*Locator.email_field).send_keys(gen_email())
        general_settings.find_element(*Locator.password_field).send_keys(password)
        general_settings.find_element(*Locator.button_registration).click()
        WebDriverWait(general_settings, 10).until(expected_conditions.visibility_of_element_located(Locator.text_enter_in_account))
        checking_text_enter = general_settings.find_element(*Locator.text_enter_in_account).text
        assert checking_text_enter == "Вход"

    def test_login_through_page_password_recovery (self, general_settings):
        general_settings.find_element(*Locator.button_personal_account).click()
        general_settings.find_element(*Locator.sign_recovery_password).click()
        general_settings.find_element(*Locator.button_enter_in_recovery_page).click()
        general_settings.find_element(*Locator.email_field).send_keys(email)
        general_settings.find_element(*Locator.password_field).send_keys(password)
        general_settings.find_element(*Locator.button_enter).click()
        WebDriverWait(general_settings, 3).until(expected_conditions.visibility_of_element_located(Locator.text_in_main_page))
        checking_text_main_page = general_settings.find_element(*Locator.text_in_main_page).text
        assert checking_text_main_page == 'Оформить заказ'








