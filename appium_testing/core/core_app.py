from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class App:
    def __init__(self, options):
        self.__driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    def get_by_id(self, locator):
        return self.__driver.find_element(AppiumBy.ID, locator)

    def get_by_xpath(self, locator):
        return self.__driver.find_element(AppiumBy.XPATH, locator)

    def get_by_uiautomator(self, locator):
        """
        Method to find an element by new UiSelector()
        :param locator: must be a string in the format 'method("locator")' without new UiSelector()
        :return: element
        """
        return self.__driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, locator)

    def get_elements_by_xpath(self, locator):
        return self.__driver.find_elements(AppiumBy.XPATH, locator)

    def press_enter(self):
        self.__driver.press_keycode(66)

    def wait(self, sec):
        self.__driver.implicitly_wait(sec)

    def wait_for_element_to_be_clickable(self, method, locator, sec):
        wait = WebDriverWait(self.__driver, sec)
        match method:
            case "ID":
                wait.until(EC.element_to_be_clickable((AppiumBy.ID, locator)))
            case "UI_AUTOMATOR":
                wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, locator)))
            case "XPATH":
                wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, locator)))

    def quit(self):
        self.__driver.quit()