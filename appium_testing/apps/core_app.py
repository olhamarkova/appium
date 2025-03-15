from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class App:
    def __init__(self, options):
        self.__driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        self.__actions = ActionChains(self.__driver)

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

    def get_scrollable_element_by_text(self, text):
        return self.__driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains(\""+text+"\").instance(0))")

    def open_url(self, url):
        self.__driver.get(url)

    def _get_title(self):
        return self.__driver.title

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

    def wait_for_element_to_be_visible(self, method, locator, sec):
        wait = WebDriverWait(self.__driver, sec)
        match method:
            case "ID":
                wait.until(EC.visibility_of_element_located((AppiumBy.ID, locator)))
            case "UI_AUTOMATOR":
                wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locator)))
            case "XPATH":
                wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, locator)))

    def quit(self):
        self.__driver.quit()

    def swipe_up(self, count):
        for i in range(1, count):
            print(f"I swipe {i} time(s)")
            self.__driver.swipe(514,600,514,200,1000)

    def swipe_down(self, count):
        for i in range(1, count):
            print(f"I swipe {i} time(s)")
            self.__driver.swipe(514, 500, 514, 800, 1000)

    def long_tap(self, element):
        self.__actions.click_and_hold(element)
        self.__actions.perform()