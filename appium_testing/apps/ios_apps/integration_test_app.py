from appium_testing.apps.core_app import App
import logging

logger = logging.getLogger(__name__)


class IntegrationApp(App):
    def __init__(self, options):
        super().__init__(options)

    def __back_button(self):
        return self.get_by_accessibility_id('Back')

    def __alerts_link(self):
        return self.get_by_xpath('//XCUIElementTypeStaticText[@name="Alerts"]')

    def __attributes_link(self):
        return self.get_by_accessibility_id('Attributes')

    def __alerts_text_filed(self):
        return self.get_by_xpath('//XCUIElementTypeTextField[@name="textField"]')

    def __create_app_alert_link(self):
        return self.get_by_accessibility_id('Create App Alert')

    def __app_alert(self):
        return self.get_by_xpath('//XCUIElementTypeAlert[@name="Magic"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]')

    def __will_do_button(self):
        return self.get_by_accessibility_id('Will do')

    def __attributes_value_input(self):
        return self.get_by_xpath('//XCUIElementTypeTextField[1]')

    def __switch(self):
        return self.get_element_by_class('XCUIElementTypeSwitch')


    def open_alerts_page(self):
        self.__alerts_link().click()

    def open_attributes_page(self):
        self.__attributes_link().click()

    def fill_alert_test_field(self, text):
        self.__alerts_text_filed().send_keys(text)

    def open_app_alert(self):
        self.__create_app_alert_link().click()

    def close_app_alert(self):
        self.__will_do_button().click()

    def go_back(self):
        self.__back_button().click()

    def clear_value_input(self):
        self.__attributes_value_input().clear()

    def turn_off_switch(self):
        is_switch_on = self.__switch().get_attribute("value")
        if is_switch_on == '1':
            logger.info('Turning off the switch')
            self.__switch().click()
        elif is_switch_on == '0':
            logger.info('Switch is turned off')
            pass


    def assert_alert_is_opened(self):
        assert self.__app_alert()

    def assert_main_page_is_opened(self):
        assert self.__alerts_link()

    def assert_value_is_cleared(self):
        assert not self.__attributes_value_input().get_attribute('value')

    def assert_switch_is_turned_off(self):
        is_switch_on = self.__switch().get_attribute("value")
        assert is_switch_on == '0'




