from Locators import Locator



class TestTransfersInConstructorPage:
    def test_transfer_click_on_sauce_button (self, general_settings):
        general_settings.find_element(*Locator.button_sauce).click()
        checking_text_sauce = general_settings.find_element(*Locator.text_sauce_in_scroll).text
        check_choose_item = general_settings.find_element(*Locator.choose_section_of_item).text
        assert checking_text_sauce == check_choose_item

    def test_transfer_click_on_topping_button (self, general_settings):
        general_settings.find_element(*Locator.button_topping).click()
        checking_text_topping = general_settings.find_element(*Locator.text_topping_in_scroll).text
        check_choose_item = general_settings.find_element(*Locator.choose_section_of_item).text
        assert checking_text_topping == check_choose_item

    def test_transfer_click_on_bread_button (self, general_settings):
        general_settings.find_element(*Locator.button_bread).click()
        checking_text_bread = general_settings.find_element(*Locator.text_bread_in_scroll).text
        check_choose_item = general_settings.find_element(*Locator.choose_section_of_item).text
        assert checking_text_bread == check_choose_item
