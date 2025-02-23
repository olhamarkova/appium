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
