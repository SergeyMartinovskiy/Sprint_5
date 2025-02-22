from Locators import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from my_data import *

class TestRegistration:
    def test_correct_registration (self, general_settings):
        general_settings.find_element(*Locator.button_personal_account).click()
        general_settings.find_element(*Locator.sign_registration).click()
        general_settings.find_element(*Locator.name_field).send_keys(user_name)
        general_settings.find_element(*Locator.email_field).send_keys(gen_email())
        general_settings.find_element(*Locator.password_field).send_keys(password)
        general_settings.find_element(*Locator.button_registration).click()
        WebDriverWait(general_settings, 10).until(expected_conditions.visibility_of_element_located(Locator.text_enter_in_account))
        checking_text_enter = general_settings.find_element(*Locator.text_enter_in_account).text
        assert checking_text_enter == "Вход"

    def test_incorrect_registration_with_wrong_password (self, general_settings):
        general_settings.find_element(*Locator.button_personal_account).click()
        general_settings.find_element(*Locator.sign_registration).click()
        general_settings.find_element(*Locator.name_field).send_keys(user_name)
        general_settings.find_element(*Locator.email_field).send_keys(email)
        general_settings.find_element(*Locator.password_field).send_keys(invalid_password)
        general_settings.find_element(*Locator.button_registration).click()
        WebDriverWait(general_settings, 10).until(expected_conditions.visibility_of_element_located(Locator.text_invalid_password))
        uncorrect_password = general_settings.find_element(*Locator.text_invalid_password).text
        assert uncorrect_password == "Некорректный пароль"
