import pytest
import time
from appium_testing.utils.config_reader import get_config_property
from appium_testing.apps.web_app.web_app import WebApp
from appium_testing.utils.capabilities_profiles import chrome


wiki_url = get_config_property("basic", "wiki_url")


@pytest.mark.functional
def test_open_random_fact(app_factory):
    with app_factory(WebApp, chrome) as web_app:
        web_app.open_url(f"{wiki_url}")
        web_app.open_menu()
        web_app.go_to_random()

        web_app.assert_title()

        time.sleep(2)
