from pathlib import Path
from appium.options.android import UiAutomator2Options
import logging
from appium.options.ios import XCUITestOptions

logger = logging.getLogger(__name__)

DEFAULT_CAPS = {
    "deviceName": "Android Emulator",
    "automationName": "UiAutomator2",
    "platformNames": ["Android"],
    "adbExecTimeout": 60000
}

def create_android_capabilities(overrides: dict = None) -> UiAutomator2Options:
    capabilities = DEFAULT_CAPS.copy()

    if overrides:
        capabilities.update(overrides)

    app_path = capabilities.get("app")
    if app_path:
        full_app_path = Path(__file__).parent.parent / app_path
        capabilities["app"] = str(full_app_path.resolve())

    logger.info(f"Final capabilities: {capabilities}")

    return UiAutomator2Options().load_capabilities(capabilities)

def create_ios_capabilities() -> XCUITestOptions:
    options = XCUITestOptions()
    options.set_capability('platformName', 'iOS')
    options.set_capability('platformVersion', '18.4')
    options.set_capability('deviceName', 'iPhone 16 Pro')
    options.set_capability('udid', '1AD48EFE-B353-4DC0-8BA5-E0D72F23D9D6')
    options.set_capability('bundleId', 'com.olha.IntegrationApp')
    options.set_capability('noReset', True)
    options.set_capability('automationName', 'XCUITest')
    options.set_capability("useNewWDA", True)

    return options