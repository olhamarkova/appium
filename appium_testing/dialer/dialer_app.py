from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class DialerApp:
    def __init__(self, options):
        self.__driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    def __dialer_tab(self):
        return self.__driver.find_element(AppiumBy.ID, "com.google.android.dialer:id/dialpad_fab")

    def __digit_button(self, digit):
        return self.__driver.find_element(AppiumBy.ID, f"com.google.android.dialer:id/{digit}")

    def __call_button(self):
        return self.__driver.find_element(AppiumBy.ID, "com.google.android.dialer:id/dialpad_voice_call_button")

    def __end_call_button(self):
        return self.__driver.find_element(AppiumBy.ID, "com.google.android.dialer:id/incall_end_call")

    def click_digit_button(self, digit):
        self.__digit_button(digit).click()

    def open_dialer(self):
        self.__dialer_tab().click()

    def make_call(self):
        self.__call_button().click()

    def end_call(self):
        self.__end_call_button().click()

    def wait(self, sec):
        self.__driver.implicitly_wait(sec)

    def quit(self):
        self.__driver.quit()
