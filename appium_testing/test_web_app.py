import time

from appium_testing.apps.web_app.web_app import WebApp
from utils.server_launching import stop_appium_server
from utils.capabilities_builder import load_capabilities, app_capabilities

desired_caps = app_capabilities(browserName="Chrome", automationName="UiAutomator2")
capabilities_options = load_capabilities(desired_caps)

wiki = WebApp(capabilities_options)

wiki.open_url("https://commons.m.wikimedia.org/wiki/Main_Page")

wiki.open_menu()
wiki.go_to_random()
wiki.assert_title()

time.sleep(2)

wiki.quit()
stop_appium_server()