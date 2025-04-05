import pytest
from appium_testing.utils.server_launching import start_appium_server, stop_appium_server
from appium_testing.utils.desired_caps import app_capabilities, load_capabilities
from appium_testing.apps.contacts.contacts_app import ContactsApp

@pytest.fixture(scope="module")
def setup():
    start_appium_server()

    yield
    stop_appium_server()
    print("server stopped")

@pytest.fixture(scope="module")
def get_app():
    desired_caps = app_capabilities(appPackage="com.google.android.dialer",
                                    appActivity=".extensions.GoogleDialtactsActivity")
    capabilities_options = load_capabilities(desired_caps)
    contact = ContactsApp(capabilities_options)
    return contact

@pytest.mark.usefixtures("setup", "get_app")
def test_add_new_contact():
    print('Pytest test')