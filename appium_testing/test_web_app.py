import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from core.desired_caps import get_web_capabilities

desired_caps = get_web_capabilities()

# start server
appium_service = AppiumService()
appium_service.start()
print(appium_service.is_running)
print(appium_service.is_listening)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://127.0.0.1:4723", options = capabilities_options)

# automate web app (Google Chrome)
driver.get("https://commons.m.wikimedia.org/wiki/Main_Page")

driver.find_element(AppiumBy.XPATH, "//label[@for='main-menu-input']").click()

driver.find_element(AppiumBy.XPATH, "//li/a[contains(., 'Random')]").click()
print(driver.title)
title = driver.title
for word in title.split():
    assert "File:" in word
    print('Here it is!')
    break

time.sleep(2)

# stop the server
driver.quit()
appium_service.stop()