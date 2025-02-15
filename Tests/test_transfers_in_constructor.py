from Locators import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from my_data import *

class TestTransfersInConstructorPage:
    def test_transfer_click_on_sauce_button (self, general_settings):
        general_settings.find_element(*Locator.button_sauce).click()
        checking_text_sauce = general_settings.find_element(*Locator.text_sauce_in_scroll ).text
        check_choose_item = general_settings.find_element(*Locator.choose_section_of_item).text
        assert checking_text_sauce == check_choose_item
