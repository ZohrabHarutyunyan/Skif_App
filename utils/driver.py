from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from utils.date_reader import data_reader


class Driver:
    @staticmethod
    def get_driver():
        config = data_reader()
        if config["browser"] == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            option = webdriver.ChromeOptions()
            if config["headless_mode"] is True:
                option.add_argument("--headless")
            driver = webdriver.Chrome(service=service, options=option)
            return driver
        elif config["browser"] == "firefox":
            options = webdriver.FirefoxOptions()
            if config["headless_mode"] is True:
                options.headless = True
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
            return driver
        raise Exception("Provide valid driver name")






