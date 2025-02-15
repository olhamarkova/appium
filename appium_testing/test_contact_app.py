import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(

    deviceName="Android",
    platformName="Android",
    appPackage="com.google.android.dialer",
    appActivity=".extensions.GoogleDialtactsActivity"

)

#start server
appium_service = AppiumService()
appium_service.start()
print(appium_service.is_running)
print(appium_service.is_listening)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://127.0.0.1:4723", options = capabilities_options)

# add a contact
driver.find_element(AppiumBy.ID, "com.google.android.dialer:id/tab_contacts").click()
driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.google.android.dialer:id/contact_name' and @text='Create new contact']").click()
driver.implicitly_wait(1)
driver.find_element(AppiumBy.XPATH, '//*[contains(@text, "First name")]').send_keys("John")

driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Last name']").send_keys("Doe")
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='+1']").send_keys("123456789")

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Save']").click()

driver.quit()
appium_service.stop()