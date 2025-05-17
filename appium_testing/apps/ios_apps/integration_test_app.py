from appium_testing.apps.core_app import App


class IntegrationApp(App):
    def __init__(self, options):
        super().__init__(options)

    def __back_button(self):
        return self.get_by_accessibility_id('Back')

    def __alerts_link(self):
        return self.get_by_xpath('//XCUIElementTypeStaticText[@name="Alerts"]')

    def __alerts_text_filed(self):
        return self.get_by_xpath('//XCUIElementTypeTextField[@name="textField"]')

    def __create_app_alert_link(self):
        return self.get_by_accessibility_id('Create App Alert')

    def __app_alert(self):
        return self.get_by_xpath('//XCUIElementTypeAlert[@name="Magic"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]')

    def __will_do_button(self):
        return self.get_by_accessibility_id('Will do')


    def open_alerts_page(self):
        self.__alerts_link().click()

    def fill_alert_test_field(self, text):
        self.__alerts_text_filed().send_keys(text)

    def open_app_alert(self):
        self.__create_app_alert_link().click()

    def close_app_alert(self):
        self.__will_do_button().click()

    def go_back(self):
        self.__back_button().click()

    def assert_alert_is_opened(self):
        assert self.__app_alert()

    def assert_main_page_is_opened(self):
        assert self.__alerts_link()




