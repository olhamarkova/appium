import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

from appium_testing.contacts.contacts_app import ContactsApp
from core.server_launching import start_appium_server, stop_appium_server
from core.desired_caps import get_app_capabilities, load_capabilities

# setup
desired_caps = get_app_capabilities("com.google.android.dialer", ".extensions.GoogleDialtactsActivity")
start_appium_server()
capabilities_options = load_capabilities(desired_caps)

contact = ContactsApp(capabilities_options)

#test
contact.open_contacts_tab()
number_of_contacts_before = contact.get_numbers_count()
contact.open_new_contact_form()
contact.wait(1)

contact.enter_name("First name", "John")
contact.enter_name("Last name", "Doe")
contact.enter_number("234567891")

contact.save_number()
number_of_contacts_after = contact.get_numbers_count()

assert number_of_contacts_after - 1 == number_of_contacts_before

contact.quit()
stop_appium_server()


# desired_caps = dict(
#
#     deviceName="Android",
#     platformName="Android",
#     appPackage="com.google.android.dialer",
#     appActivity=".extensions.GoogleDialtactsActivity"
#
# )

#start server
# appium_service = AppiumService()
# appium_service.start()
# print(appium_service.is_running)
# print(appium_service.is_listening)
#
# capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
# driver = webdriver.Remote("http://127.0.0.1:4723", options = capabilities_options)

# add a contact
# driver.find_element(AppiumBy.ID, "com.google.android.dialer:id/tab_contacts").click()
# driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.google.android.dialer:id/contact_name' and @text='Create new contact']").click()
# driver.implicitly_wait(1)
# driver.find_element(AppiumBy.XPATH, '//*[contains(@text, "First name")]').send_keys("John")
#
# driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Last name']").send_keys("Doe")
# driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='+1']").send_keys("123456789")
#
# driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Save']").click()
#
# driver.quit()
# appium_service.stop()