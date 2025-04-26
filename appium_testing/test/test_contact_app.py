import pytest
import logging
from appium_testing.apps.contacts.contacts_app import ContactsApp

logger = logging.getLogger(__name__)

contact_app_capabilities = {
    "appPackage": "com.google.android.dialer",
    "appActivity": ".extensions.GoogleDialtactsActivity",
}

def get_data():
    return [
        ("Jane", "Doe", "234567891"),
        ("John", "Foo", "334456778"),
        ("Karen", "Smith", "235458990")
    ]

@pytest.mark.usefixtures("setup")
@pytest.mark.functional
@pytest.mark.parametrize("first_name, last_name, phone_number", get_data())
def test_add_new_contact(app_factory, first_name, last_name, phone_number):
    with app_factory(ContactsApp, contact_app_capabilities) as contact_app:
        contact_app.open_contacts_tab()
        logger.info(f"Contact app is opened")
        number_of_contacts_before = contact_app.get_numbers_count()
        contact_app.open_new_contact_form()
        contact_app.wait(1)
        contact_app.enter_name("First name", first_name)
        contact_app.enter_name("Last name", last_name)
        contact_app.enter_number(phone_number)
        contact_app.save_number()
        logger.info(f"Contact {first_name} {last_name} is saved")
        number_of_contacts_after = contact_app.get_numbers_count()

        assert number_of_contacts_before + 1 == number_of_contacts_after

@pytest.mark.smoke
@pytest.mark.parametrize("first_name, last_name, phone_number", get_data())
def test_open_contact(app_factory, normalize_phone, first_name, last_name, phone_number):
    with app_factory(ContactsApp, contact_app_capabilities) as contact_app:
        contact_app.open_contacts_tab()
        logger.info(f"Contact app is opened")
        contact_app.scroll_and_open_contact(f"{first_name} {last_name}")
        contact_app.wait_contact_opened()
        logger.info(f"Contact {first_name} {last_name} is opened")
        contact_name = contact_app.get_number_title_text()
        number = contact_app.get_contact_number()

        assert normalize_phone(number) == normalize_phone(phone_number)
        assert contact_name == f"{first_name} {last_name}"


@pytest.mark.smoke
@pytest.mark.parametrize("first_name, last_name, phone_number", get_data())
def test_delete_contact(app_factory, normalize_phone, first_name, last_name, phone_number):
    with app_factory(ContactsApp, contact_app_capabilities) as contact_app:
        contact_app.open_contacts_tab()
        logger.info(f"Contact app is opened")
        number_of_contacts_before = contact_app.get_numbers_count()
        contact_app.open_contact(f"{first_name} {last_name}")
        contact_app.wait_contact_opened()
        logger.info(f"Contact {first_name} {last_name} is opened")
        contact_app.delete_number()
        contact_app.wait_contact_deleted(f"{first_name} {last_name}", 5)
        logger.info(f"Contact {first_name} {last_name} is deleted")
        number_of_contacts_after = contact_app.get_numbers_count()

        assert number_of_contacts_before - 1 == number_of_contacts_after
