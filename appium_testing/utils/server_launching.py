from appium.webdriver.appium_service import AppiumService

class AppiumManager:
    def __init__(self):
        self.appium_service = AppiumService()

    def start_appium_server(self, args):
        self.appium_service.start()

    def stop_appium_server(self):
        self.appium_service.stop()