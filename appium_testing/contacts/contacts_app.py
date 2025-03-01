from appium_testing.core.core_app import App

class ContactsApp(App):
    def __init__(self, options):
        super().__init__(options)

    def __contacts_tab(self):
        return self.get_by_id("com.google.android.dialer:id/tab_contacts")

    def __create_contact_btn(self):
        return self.get_by_xpath("//android.widget.TextView[@resource-id='com.google.android.dialer:id/contact_name' and @text='Create new contact']")

    def __name_input(self, input_placeholder):
        return self.get_by_xpath(f"//*[contains(@text, '{input_placeholder}')]")

    def __number_input(self):
        return self.get_by_xpath("//android.widget.EditText[@text='+1']")

    def __save_btn(self):
        return self.get_by_xpath("//android.widget.TextView[@text='Save']")

    def __contact_name(self):
        return self.get_by_id("com.google.android.contacts:id/large_title")

    def get_numbers_count(self):
        length = len(self.get_elements_by_xpath('//android.widget.LinearLayout[@resource-id="com.google.android.dialer:id/click_target"]'))
        print(length)
        return length

    def get_number_title_text(self):
        text = self.get_by_id("com.google.android.contacts:id/large_title").get_attribute("text")
        print(text)
        return text

    def open_contacts_tab(self):
        self.__contacts_tab().click()

    def open_contact(self, name):
        self.get_scrollable_element_by_text(name).click()

    def open_new_contact_form(self):
        self.__create_contact_btn().click()

    def enter_name(self, input_placeholder, name):
        self.__name_input(input_placeholder).send_keys(name)

    def enter_number(self, number):
        self.__number_input().send_keys(number)

    def save_number(self):
        self.__save_btn().click()

    def wait_contact_opened(self):
        self.wait_for_element_to_be_visible("ID", "com.google.android.contacts:id/large_title", 10)