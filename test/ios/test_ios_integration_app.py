import pytest
from apps.ios_apps.integration_app import IntegrationApp
from utils.capabilities_profiles import ios_test_app


@pytest.mark.use_appium
@pytest.mark.functional
def test_alerts(app_factory):
    with app_factory(IntegrationApp, "ios", ios_test_app) as app:
        app.open_alerts_screen()
        app.fill_alert_test_field('test')
        app.open_app_alert()
        app.assert_alert_is_opened()

        app.close_app_alert()
        app.go_back()
        app.assert_main_page_is_opened()


@pytest.mark.smoke
def test_input(app_factory):
    with app_factory(IntegrationApp, "ios", ios_test_app) as app:
        app.open_attributes_screen()
        app.clear_value_input()
        app.assert_value_is_cleared()

        app.go_back()


@pytest.mark.functional
def test_switches(app_factory):
    with app_factory(IntegrationApp, "ios", ios_test_app) as app:
        app.open_attributes_screen()
        app.turn_off_switch()
        app.assert_switch_is_turned_off()

        app.go_back()


@pytest.mark.functional
def test_steppers(app_factory):
    with app_factory(IntegrationApp, "ios", ios_test_app) as app:
        app.open_attributes_screen()
        app.click_stepper_button("Increment")
        app.assert_stepper_button_enabled("Decrement", True)
        app.click_stepper_button("Decrement")
        app.assert_stepper_button_enabled("Decrement", False)

        app.go_back()


@pytest.mark.functional
def test_sliders(app_factory):
    with app_factory(IntegrationApp, "ios", ios_test_app) as app:
        app.open_attributes_screen()
        app.change_slider(0.2)
        app.assert_slider_value(20)

        app.go_back()


@pytest.mark.functional
def test_date_picker_wheel(app_factory):
    with app_factory(IntegrationApp, "ios", ios_test_app) as app:
        app.open_attributes_screen()
        app.select_day_on_picker_wheel()
        app.set_date(1, "15")
        app.set_date(2, "06")

        app.go_back()