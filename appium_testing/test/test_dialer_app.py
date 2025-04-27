import pytest
from appium_testing.apps.dialer.dialer_app import DialerApp
from appium_testing.utils.capabilities_profiles import contact_app_caps


@pytest.mark.functional
def test_make_call(app_factory):
    with app_factory(DialerApp, contact_app_caps) as dialer_app:
        dialer_app.wait_for_recents()
        dialer_app.open_recents()
        dialer_app.open_dialer()

        dialer_app.click_digit_button("one")
        dialer_app.click_digit_button("seven")
        dialer_app.click_digit_button("three")
        dialer_app.click_digit_button("five")

        dialer_app.make_call()
        dialer_app.wait(2)
        dialer_app.end_call()

        """
        TODO:
        add assertions
        """