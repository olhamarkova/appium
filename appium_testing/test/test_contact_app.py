import pytest
from appium_testing.apps.android_apps.contacts.contacts_app import ContactsApp
from appium_testing.utils.capabilities_profiles import dialer

def get_data():
    return [
        ("Jane", "Doe", "234567891"),
        # ("John", "Foo", "334456778"),
        # ("Karen", "Smith", "235458990")
    ]


@pytest.mark.use_appium
@pytest.mark.functional
@pytest.mark.parametrize("first_name, last_name, phone_number", get_data())
def test_add_new_contact(app_factory, first_name, last_name, phone_number):
    with app_factory(ContactsApp, "android", dialer) as contact_app:
        contact_app.open_contacts_tab()
        number_of_contacts_before = contact_app.get_numbers_count()
        contact_app.open_new_contact_form()
        contact_app.wait(1)
        contact_app.enter_name("First name", first_name)
        contact_app.enter_name("Last name", last_name)
        contact_app.enter_number(phone_number)
        contact_app.save_number()
        number_of_contacts_after = contact_app.get_numbers_count()

        contact_app.assert_contact_is_added(number_of_contacts_before, number_of_contacts_after)


@pytest.mark.use_appium
@pytest.mark.smoke
@pytest.mark.parametrize("first_name, last_name, phone_number", get_data())
def test_open_contact(app_factory, first_name, last_name, phone_number):
    with app_factory(ContactsApp, "android", dialer) as contact_app:
        full_name = f"{first_name} {last_name}"
        contact_app.open_contacts_tab()
        contact_app.scroll_and_open_contact(full_name)
        contact_app.wait_contact_opened()
        contact_name = contact_app.get_number_title_text()
        saved_number = contact_app.get_contact_number()

        contact_app.assert_number_is_correct(full_name, contact_name)
        contact_app.assert_number_is_correct(saved_number, phone_number)


@pytest.mark.use_appium
@pytest.mark.functional
@pytest.mark.parametrize("first_name, last_name, phone_number", get_data())
def test_delete_contact(app_factory, first_name, last_name, phone_number):
    with app_factory(ContactsApp, "android", dialer) as contact_app:
        full_name = f"{first_name} {last_name}"
        contact_app.open_contacts_tab()
        number_of_contacts_before = contact_app.get_numbers_count()
        contact_app.open_contact(full_name)
        contact_app.wait_contact_opened()
        contact_app.delete_number()
        contact_app.wait_contact_deleted(full_name, 5)
        number_of_contacts_after = contact_app.get_numbers_count()

        contact_app.assert_contact_is_deleted(number_of_contacts_before, number_of_contacts_after)
