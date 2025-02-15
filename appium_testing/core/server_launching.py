from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options

appium_service = AppiumService()

def start_appium_server():
    appium_service.start()
    print(f"Server is running: {appium_service.is_running}")

def stop_appium_server():
    appium_service.stop()