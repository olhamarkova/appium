from utils.adb_runner import run_adb_command
import logging


logger = logging.getLogger(__name__)


class AppManager():
    def __init__(self, package):
        self.package = package


    def uninstall_app(self):
        logger.info(f"Uninstalling application")
        run_adb_command(f"uninstall {self.package}")


    def is_app_installed(self):
        logger.info(f"Verifying packages...")
        output = run_adb_command(f"shell cmd package list packages -3")
        return f"package:{self.package}" in output


    def assert_app_is_uninstalled(self):
        assert not self.is_app_installed()