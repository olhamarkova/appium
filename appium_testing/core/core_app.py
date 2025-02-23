from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class App:
    def __init__(self, options):
        self.__driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    def get_by_id(self, locator):
        return self.__driver.find_element(AppiumBy.ID, locator)

    def get_by_xpath(self, locator):
        return self.__driver.find_element(AppiumBy.XPATH, locator)

    def get_elements_by_xpath(self, locator):
        return self.__driver.find_elements(AppiumBy.XPATH, locator)

    def wait(self, sec):
        self.__driver.implicitly_wait(sec)

    def quit(self):
        self.__driver.quit()