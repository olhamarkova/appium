from appium_testing.core.core_app import App

class DialerApp(App):
    def __init__(self, options):
        super().__init__(options)

    def __dialer_tab(self):
        return self.get_by_id("com.google.android.dialer:id/dialpad_fab")

    def __digit_button(self, digit):
        return self.get_by_id(f"com.google.android.dialer:id/{digit}")

    def __call_button(self):
        return self.get_by_id("com.google.android.dialer:id/dialpad_voice_call_button")

    def __end_call_button(self):
        return self.get_by_id("com.google.android.dialer:id/incall_end_call")

    def click_digit_button(self, digit):
        self.__digit_button(digit).click()

    def open_dialer(self):
        self.__dialer_tab().click()

    def make_call(self):
        self.__call_button().click()

    def end_call(self):
        self.__end_call_button().click()


