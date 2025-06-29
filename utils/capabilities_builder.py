from pathlib import Path
from appium.options.android import UiAutomator2Options
import logging
from appium.options.ios import XCUITestOptions

logger = logging.getLogger(__name__)

DEFAULT_ANDROID_CAPS = {
    "deviceName": "Android Emulator",
    "automationName": "UiAutomator2",
    "platformNames": ["Android"],
    "adbExecTimeout": 60000
}

DEFAULT_IOS_CAPS = {
    'automationName': 'XCUITest',
    'platformName': 'iOS',
    'useNewWDA': True,
    'noReset': True
}

def create_android_capabilities(overrides: dict = None) -> UiAutomator2Options:
    capabilities = DEFAULT_ANDROID_CAPS.copy()

    if overrides:
        capabilities.update(overrides)

    app_path = capabilities.get("app")
    if app_path:
        full_app_path = Path(__file__).parent.parent / app_path
        capabilities["app"] = str(full_app_path.resolve())

    logger.info(f"Final capabilities: {capabilities}")

    return UiAutomator2Options().load_capabilities(capabilities)


def create_ios_capabilities(overrides: dict) -> XCUITestOptions:
    capabilities = DEFAULT_IOS_CAPS.copy()
    capabilities.update(overrides)

    logger.info(f"Final capabilities: {capabilities}")

    options = XCUITestOptions()

    for key, value in capabilities.items():
        options.set_capability(key, value)

    return options