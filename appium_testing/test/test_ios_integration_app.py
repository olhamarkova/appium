import pytest
from appium_testing.apps.ios_apps.integration_test_app import IntegrationApp

@pytest.mark.functional
def test_integration_app(app_factory):
    with app_factory(IntegrationApp, "ios") as app:
        app.open_alerts_page()
        app.fill_alert_test_field('test')
        app.open_app_alert()
        app.assert_alert_is_opened()
        app.close_app_alert()
        app.go_back()
        app.assert_main_page_is_opened()
        app.open_attributes_page()
        app.clear_value_input()
        app.assert_value_is_cleared()
