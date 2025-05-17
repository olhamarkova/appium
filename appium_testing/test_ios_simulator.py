import time

from appium.options.ios import XCUITestOptions
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

options = XCUITestOptions()
options.set_capability('platformName', 'iOS')
options.set_capability('platformVersion', '18.4')
options.set_capability('deviceName', 'iPhone 16 Pro')
options.set_capability('udid', '1AD48EFE-B353-4DC0-8BA5-E0D72F23D9D6')
options.set_capability('bundleId', 'com.olha.IntegrationApp')
options.set_capability('noReset', True)

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
driver.implicitly_wait(5)

driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Alerts"]').click()
driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="textField"]').send_keys('test')
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Create App Alert').click()
assert driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeAlert[@name="Magic"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]')
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Will do').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Back').click()
assert driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Alerts"]')
time.sleep(5)
driver.quit()
