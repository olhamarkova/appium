from appium.options.android import UiAutomator2Options


def get_app_capabilities(package, activity):
    capabilities = {
        "deviceName": "Android",
        "platformName": "Android",
        "appPackage": package,
        'appActivity': activity
    }
    return capabilities

def get_web_capabilities():
    capabilities = dict(
        deviceName = "Android",
        platformName = "Android",
        browserName = "Chrome",
        automationName = "UiAutomator2"
    )
    return capabilities

def load_capabilities(desired_caps):
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    return capabilities_options