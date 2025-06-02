from apps.core_app import App
import logging

logger = logging.getLogger(__name__)


class IntegrationApp(App):
    def __init__(self, options):
        super().__init__(options)


    # Elements
    def __back_button(self):
        return self.get_by_accessibility_id('Back')


    def __alerts_link(self):
        return self.get_by_xpath('//XCUIElementTypeStaticText[@name="Alerts"]')


    def __attributes_link(self):
        return self.get_by_accessibility_id('Attributes')

    '''
    Alerts screen
    '''

    def __alerts_text_filed(self):
        return self.get_by_xpath('//XCUIElementTypeTextField[@name="textField"]')


    def __create_app_alert_link(self):
        return self.get_by_accessibility_id('Create App Alert')


    def __app_alert(self):
        return self.get_by_xpath('//XCUIElementTypeAlert[@name="Magic"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]')


    def __will_do_button(self):
        return self.get_by_accessibility_id('Will do')

    '''
    Attributes screen
    '''

    def __attributes_value_input(self):
        return self.get_by_xpath('//XCUIElementTypeTextField[1]')


    def __switch(self):
        return self.get_element_by_class('XCUIElementTypeSwitch')


    def __steppers(self, name):
        return self.get_by_xpath(f'//XCUIElementTypeButton[@name="{name}"]')


    def __slider(self):
        return self.get_element_by_class('XCUIElementTypeSlider')


    def __date_picker_wheel(self, index):
        return self.get_elements_by_class('XCUIElementTypePickerWheel')[index]


    # Actions
    def open_alerts_screen(self):
        logger.info("Open Alerts screen")
        self.__alerts_link().click()


    def open_attributes_screen(self):
        logger.info("Open Attributes screen")
        self.__attributes_link().click()


    def go_back(self):
        logger.info("Go to Home screen")
        self.__back_button().click()


    def fill_alert_test_field(self, text):
        logger.info(f"Typing text {text}")
        self.__alerts_text_filed().send_keys(text)


    def open_app_alert(self):
        logger.info("Open alert")
        self.__create_app_alert_link().click()


    def close_app_alert(self):
        logger.info("Close alert")
        self.__will_do_button().click()


    def clear_value_input(self):
        logger.info("Clear input")
        self.__attributes_value_input().clear()


    def turn_off_switch(self):
        is_switch_on = self.__switch().get_attribute("value")
        if is_switch_on == "1":
            logger.info("Turning off the switch")
            self.__switch().click()
        elif is_switch_on == "0":
            logger.info("Switch is turned off")
            pass


    def click_stepper_button(self, name):
        logger.info(f"Clicking the {name} button")
        self.__steppers(name).click()


    def change_slider(self, value):
        logger.info(f"Changing slider to {value}")
        self.__slider().send_keys(value)


    def select_day_on_picker_wheel(self):
        self.execute_script("mobile: selectPickerWheelValue", {'order': 'next', 'offset': 0.15, 'element': self.__date_picker_wheel(0)})


    def set_date(self, index, data):
        self.__date_picker_wheel(index).send_keys(data)


    # Assertions
    def assert_alert_is_opened(self):
        assert self.__app_alert()


    def assert_main_page_is_opened(self):
        assert self.__alerts_link()


    def assert_value_is_cleared(self):
        assert not self.__attributes_value_input().get_attribute("value")


    def assert_switch_is_turned_off(self):
        is_switch_on = self.__switch().get_attribute("value")
        assert is_switch_on == "0"


    def assert_stepper_button_enabled(self, name, enabled):
        is_button_enabled = self.__steppers(name).get_attribute("enabled")
        if enabled:
            assert is_button_enabled == "true"
            logger.info(f"Button {name} is enabled")
        elif not enabled:
            assert is_button_enabled == "false"
            logger.info(f"Button {name} is disabled")


    def assert_slider_value(self, value):
        slider_value = self.__slider().get_attribute("value")
        final_value = int(slider_value[0:2])
        logger.info(f"Slider value is {final_value}")
        assert final_value in range(value - 3, value + 3)
