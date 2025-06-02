from appium_testing.apps.android_apps.cossacks_game.cossacks_game import CossacksGame

# setup
desired_caps = app_capabilities(app="appium_testing/app/cossacks.apk")
start_appium_server()
capabilities_options = load_capabilities(desired_caps)

cossacks = CossacksGame(capabilities_options)
cossacks.wait(5)
cossacks.quit()
stop_appium_server()