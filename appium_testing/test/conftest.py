from typing import Type
import pytest
import re
import time
import logging
from contextlib import contextmanager
from appium_testing.utils.server_launching import AppiumManager
from appium_testing.utils.capabilities_builder import create_capabilities

logger = logging.getLogger(__name__)
appium = AppiumManager()

def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: "%(message)s"',
    )

@pytest.fixture(scope="session", autouse=True)
def appium_server():
    if appium.appium_service.is_running:
        logger.info("Appium server already running, reusing it.")
    else:
        appium.start_appium_server()
        logger.info("Starting Appium server...")

        time.sleep(2)

        if not appium.appium_service.is_running:
            raise RuntimeError("Appium server failed to start!")
        logger.info("Appium server started successfully.")

    try:
        yield
    finally:
        if appium.appium_service.is_running:
            appium.stop_appium_server()
            logger.info("Appium server stopped.")


@pytest.fixture(scope="function")
def app_factory():
    @contextmanager
    def _create_app(app_class: Type, overrides: dict = None):
        options = create_capabilities(overrides)
        app_instance = app_class(options)

        try:
            yield app_instance
        finally:
            app_instance.quit()

    return _create_app
