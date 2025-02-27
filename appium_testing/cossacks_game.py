from appium_testing.dialer.dialer_app import DialerApp
from core.server_launching import start_appium_server, stop_appium_server
from core.desired_caps import load_capabilities, app_capabilities

# setup
desired_caps = app_capabilities(app="appium_testing/app/cossacks.apk")
start_appium_server()
capabilities_options = load_capabilities(desired_caps)

cossacks = DialerApp(capabilities_options) #TODO: create a class for the app
cossacks.wait(5)
cossacks.quit()
stop_appium_server()