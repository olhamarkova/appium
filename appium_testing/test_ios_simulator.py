import time

from appium.options.ios import XCUITestOptions
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium_testing.apps.ios_apps.integration_test_app import IntegrationApp

options = XCUITestOptions()
options.set_capability('platformName', 'iOS')
options.set_capability('platformVersion', '18.4')
options.set_capability('deviceName', 'iPhone 16 Pro')
options.set_capability('udid', '1AD48EFE-B353-4DC0-8BA5-E0D72F23D9D6')
options.set_capability('bundleId', 'com.olha.IntegrationApp')
options.set_capability('noReset', True)

app = IntegrationApp(options)
app.wait(5)

app.open_alerts_page()
app.fill_alert_test_field('test')
app.open_app_alert()
app.assert_alert_is_opened()
app.close_app_alert()
app.go_back()
app.assert_main_page_is_opened()

time.sleep(5)
app.quit()
