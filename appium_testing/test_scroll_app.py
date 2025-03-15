from appium_testing.apps.contacts.contacts_app import ContactsApp
from utils.server_launching import start_appium_server, stop_appium_server
from utils.desired_caps import app_capabilities, load_capabilities

# setup
desired_caps = app_capabilities(appPackage="com.google.android.dialer", appActivity=".extensions.GoogleDialtactsActivity")
start_appium_server()
capabilities_options = load_capabilities(desired_caps)

contact = ContactsApp(capabilities_options)

#test
contact.open_contacts_tab()
contact.swipe_up(3)
contact.open_contact("test1 appium")
#contact.scroll_and_open_contact("test1 appium")
contact.wait_contact_opened()
contact_name = contact.get_number_title_text()
assert contact_name == "test1 appium"

contact.quit()
stop_appium_server()
