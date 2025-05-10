import pytest
from appium_testing.apps.dialer.dialer_app import DialerApp
from appium_testing.utils.capabilities_profiles import dialer


@pytest.mark.functional
def test_make_call(app_factory):
    try:
        with app_factory(DialerApp, dialer) as dialer_app:
            dialer_app.wait_for_recents()
            dialer_app.open_recents()
            dialer_app.open_dialer()

            dialer_app.click_digit_button("one")
            dialer_app.click_digit_button("seven")
            dialer_app.click_digit_button("three")
            dialer_app.click_digit_button("five")

            dialer_app.make_call()
            dialer_app.wait(2)
            dialer_app.assert_end_call_button_visible()
            dialer_app.end_call()

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise
