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

    def get_elements_by_xpath(self, locator):
        return self.__driver.find_elements(AppiumBy.XPATH, locator)

    def press_enter(self):
        self.__driver.press_keycode(66)

    def wait(self, sec):
        self.__driver.implicitly_wait(sec)

    def wait_for_element_to_be_clickable(self, locator, sec):
        wait = WebDriverWait(self.__driver, sec)
        wait.until(EC.element_to_be_clickable((By.ID, locator)))

    def quit(self):
        self.__driver.quit()