from pathlib import Path
from appium.options.android import UiAutomator2Options

def app_capabilities(**caps):
    capabilities = {
        "deviceName": "Android",
        "platformName": "Android",
    }
    for key, value in caps.items():
        if key == "app":
            capabilities[key] = f"{Path().absolute().parent}/{value}"
        else:
            capabilities[key] = value
    print(capabilities)
    return capabilities

def load_capabilities(desired_caps):
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    return capabilities_options