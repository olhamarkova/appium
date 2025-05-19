from typing import Type, Literal
import pytest
import time
import logging
from contextlib import contextmanager
from appium_testing.utils.server_launching import AppiumManager
from appium_testing.utils.capabilities_builder import create_android_capabilities, create_ios_capabilities
import mysql.connector
from dotenv import load_dotenv
import os


logger = logging.getLogger(__name__)
appium = AppiumManager()
load_dotenv()


def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: "%(message)s"',
    )


@pytest.fixture(scope="module", autouse=True)
def appium_server(request):
    """
    Starts the Appium server.
    If the test uses Chrome (web app), start with --allow-insecure chromedriver_autodownload.
    """

    if request.node.get_closest_marker("use_appium") is None:
        yield
        return

    is_web_test = any("test_web_app" in item.nodeid for item in request.session.items)

    if appium.appium_service.is_running:
        logger.info("Appium server already running, reusing it.")
    else:
        args = ["--allow-insecure", "chromedriver_autodownload"] if is_web_test else None
        logger.info(f"Starting Appium server with args: {args if args else 'None'}")
        appium.start_appium_server(args=args)

        time.sleep(10)

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
    def _create_app(app_class: Type, os_type: Literal["android", "ios"], overrides: dict | None = None):
        if os_type == "android":
            options = create_android_capabilities(overrides)
        elif os_type == "ios":
            options = create_ios_capabilities()
        else:
            raise ValueError(f"Unsupported OS type: {os_type}")

        app_instance = app_class(options)
        try:
            yield app_instance
        finally:
            app_instance.quit()

    return _create_app


@pytest.fixture(scope='function')
def db_cursor():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    cursor = connection.cursor(buffered=True)

    try:
        yield cursor
    finally:
        cursor.close()
        connection.close()