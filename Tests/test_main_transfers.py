from Locators import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from my_data import *



class TestMainTransfers:
    def test_transfer_in_main_page_to_personal_page(self, general_settings):
        general_settings.find_element(*Locator.button_personal_account).click()
        general_settings.find_element(*Locator.email_field).send_keys(email)
        general_settings.find_element(*Locator.password_field).send_keys(password)
        general_settings.find_element(*Locator.button_enter).click()
        general_settings.find_element(*Locator.button_personal_account).click()
        WebDriverWait(general_settings, 3).until(expected_conditions.visibility_of_element_located(Locator.text_in_personal_account))
        checking_text_profile_in_personal_account = general_settings.find_element(*Locator.text_in_personal_account).text
        assert checking_text_profile_in_personal_account == 'В этом разделе вы можете изменить свои персональные данные'

    def test_transfer_click_on_button_constructor(self, general_settings):
        general_settings.find_element(*Locator.button_personal_account).click()
        general_settings.find_element(*Locator.email_field).send_keys(email)
        general_settings.find_element(*Locator.password_field).send_keys(password)
        general_settings.find_element(*Locator.button_enter).click()
        general_settings.find_element(*Locator.button_personal_account).click()
        general_settings.find_element(*Locator.button_constructor).click()
        checking_text_constructor_page = general_settings.find_element(*Locator.text_in_page_constructor).text
        assert checking_text_constructor_page == 'Соберите бургер'

    def test_transfer_click_on_logo_stella_burgers (self, general_settings):
        general_settings.find_element(*Locator.button_personal_account).click()
        general_settings.find_element(*Locator.email_field).send_keys(email)
        general_settings.find_element(*Locator.password_field).send_keys(password)
        general_settings.find_element(*Locator.button_enter).click()
        general_settings.find_element(*Locator.button_personal_account).click()
        general_settings.find_element(*Locator.logo_stella_burgers).click()
        checking_text_main_page = general_settings.find_element(*Locator.text_in_main_page).text
        assert checking_text_main_page == 'Оформить заказ'

