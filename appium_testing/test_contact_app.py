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
