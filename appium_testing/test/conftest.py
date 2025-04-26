import pytest
import re
from contextlib import contextmanager
from appium_testing.utils.server_launching import start_appium_server, stop_appium_server
from appium_testing.utils.desired_caps import app_capabilities, load_capabilities

@pytest.fixture(scope="module")
def setup():
    start_appium_server()
    try:
        yield
    finally:
        stop_appium_server()


@pytest.fixture(scope="function")
def app_factory():
    @contextmanager
    def _create_app(app_class, caps: dict):
        desired_caps = app_capabilities(**caps)
        capabilities_options = load_capabilities(desired_caps)
        app_instance = app_class(capabilities_options)
        try:
            yield app_instance
        finally:
            app_instance.quit()

    return _create_app

@pytest.fixture(scope="function")
def normalize_phone():
    def _normalize(number: str) -> str:
        return re.sub(r"\D", "", number)
    return _normalize