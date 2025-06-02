from apps.core_app import App

class WebApp(App):
    def __init__(self, options):
        super().__init__(options)

    def __get_menu(self):
        return self.get_by_xpath('//*[@id="main-menu-input"]')

    def __random_fact_link(self):
        return self.get_by_xpath("//li/a[contains(., 'Random')]")

    def open_menu(self):
        self.__get_menu().click()

    def go_to_random(self):
        self.__random_fact_link().click()

    def assert_title(self):
        for word in self._get_title().split():
            assert "File:" in word
            print('Here it is!')
            break