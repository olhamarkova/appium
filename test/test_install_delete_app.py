import os

from ..apps.android_apps.cossacks_game.cossacks_game import CossacksGame
from ..utils.app_manager import AppManager
from ..utils.capabilities_profiles import cossacks
import pytest
from dotenv import load_dotenv

load_dotenv()

package_name = os.getenv('APP_PACKAGE')
run_adb_command = AppManager(package_name)


@pytest.mark.use_appium
@pytest.mark.functional
def test_install_delete_app(app_factory):
        with app_factory(CossacksGame, "android", cossacks) as cossacks_game:
             cossacks_game.wait(5)
             run_adb_command.uninstall_app()
             run_adb_command.assert_app_is_deleted()

