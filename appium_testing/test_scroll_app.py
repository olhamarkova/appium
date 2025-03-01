from appium_testing.contacts.contacts_app import ContactsApp
from core.server_launching import start_appium_server, stop_appium_server
from core.desired_caps import app_capabilities, load_capabilities

# setup
desired_caps = app_capabilities(appPackage="com.google.android.dialer", appActivity=".extensions.GoogleDialtactsActivity")
start_appium_server()
capabilities_options = load_capabilities(desired_caps)

contact = ContactsApp(capabilities_options)

#test
contact.open_contacts_tab()

contact.open_contact("test1 appium")
contact.wait(5)
contact_name = contact.get_number_title_text()
assert contact_name == "test1 appium"

contact.quit()
stop_appium_server()
