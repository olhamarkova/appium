from appium_testing.apps.cossacks_game.cossacks_game import CossacksGame
from utils.server_launching import start_appium_server, stop_appium_server
from utils.capabilities_builder import create_capabilities

# setup
desired_caps = app_capabilities(app="appium_testing/app/cossacks.apk")
start_appium_server()
capabilities_options = load_capabilities(desired_caps)

cossacks = CossacksGame(capabilities_options)
cossacks.wait(5)
cossacks.quit()
stop_appium_server()