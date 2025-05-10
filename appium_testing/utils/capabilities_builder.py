from pathlib import Path
from appium.options.android import UiAutomator2Options
import logging

logger = logging.getLogger(__name__)

DEFAULT_CAPS = {
    "deviceName": "Android Emulator",
    "automationName": "UiAutomator2",
    "platformNames": ["Android"],
    "adbExecTimeout": 60000
}

def create_capabilities(overrides: dict = None) -> UiAutomator2Options:
    capabilities = DEFAULT_CAPS.copy()

    if overrides:
        capabilities.update(overrides)

    app_path = capabilities.get("app")
    if app_path:
        full_app_path = Path(__file__).parent.parent / app_path
        capabilities["app"] = str(full_app_path.resolve())

    logger.info(f"Final capabilities: {capabilities}")

    return UiAutomator2Options().load_capabilities(capabilities)
