import time

from apps.web_app.web_app import WebApp
from utils.capabilities_profiles import chrome
from utils.server_launching import AppiumManager
from utils.capabilities_builder import create_capabilities


capabilities_options = create_capabilities(chrome)

AppiumManager().start_appium_server()

wiki = WebApp(capabilities_options)

wiki.open_url("https://commons.m.wikimedia.org/wiki/Main_Page")

wiki.open_menu()
wiki.go_to_random()
wiki.assert_title()

time.sleep(2)

wiki.quit()
AppiumManager().start_appium_server()