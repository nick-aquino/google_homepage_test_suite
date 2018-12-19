from selenium import webdriver


class DriverHelper:

    # maps browser to correct driver
    drivers = {'chrome': webdriver.Chrome, 'firefox': webdriver.Firefox}

    # default browser is firefox
    current_browser = "firefox"

    def get_driver(self):
        # returns driver for current browser
        return self.drivers[self.current_browser]
