import pytest
from appium_testing.utils.server_launching import start_appium_server, stop_appium_server
from appium_testing.utils.desired_caps import app_capabilities, load_capabilities
from appium_testing.apps.contacts.contacts_app import ContactsApp

@pytest.fixture(scope="module")
def setup():
    start_appium_server()

    yield
    stop_appium_server()

@pytest.fixture(scope="function")
def contact_app():
    desired_caps = app_capabilities(appPackage="com.google.android.dialer",
                                    appActivity=".extensions.GoogleDialtactsActivity")
    capabilities_options = load_capabilities(desired_caps)
    contact = ContactsApp(capabilities_options)
    yield contact
    contact.quit()

@pytest.mark.usefixtures("setup")
@pytest.mark.functional
def test_add_new_contact(contact_app):
    contact_app.open_contacts_tab()
    number_of_contacts_before = contact_app.get_numbers_count()
    contact_app.open_new_contact_form()
    contact_app.wait(1)
    contact_app.enter_name("First name", "John")
    contact_app.enter_name("Last name", "Doe")
    contact_app.enter_number("234567891")
    contact_app.save_number()
    number_of_contacts_after = contact_app.get_numbers_count()

    assert number_of_contacts_before + 1 == number_of_contacts_after