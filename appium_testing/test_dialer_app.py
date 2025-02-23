from core.server_launching import start_appium_server, stop_appium_server
from core.desired_caps import get_app_capabilities, load_capabilities
from dialer.dialer_app import DialerApp

# setup
desired_caps = get_app_capabilities("com.google.android.dialer", ".extensions.GoogleDialtactsActivity")
start_appium_server()
capabilities_options = load_capabilities(desired_caps)

dialer = DialerApp(capabilities_options)

# test
dialer.open_dialer()

dialer.click_digit_button("one")
dialer.click_digit_button("seven")
dialer.click_digit_button("three")
dialer.click_digit_button("five")

dialer.make_call()

dialer.wait(1)

dialer.end_call()

# cleanup
dialer.quit()
stop_appium_server()