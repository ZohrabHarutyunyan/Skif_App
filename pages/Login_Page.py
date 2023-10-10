from utils.date_reader import data_reader
from utils.driver import Driver
from locators.locators import LogInLocators
import time
from selenium.webdriver.common.by import By



class LoginPage():
    @staticmethod
    def login(login, password):
        config = data_reader()
        driver = Driver()
        driver = driver.get_driver()
        driver.get(config["base_url"])
        driver.find_element(*LogInLocators.login_input).send_keys(login)
        driver.find_element(By.XPATH, '//*[@id="passwordinput"]').send_keys(password)
        driver.find_element(*LogInLocators.login_button).click()
        return driver

    @staticmethod
    def check_username():
        driver = LoginPage.login(LogInLocators.username, LogInLocators.password)
        time.sleep(1)
        username = driver.find_element(*LogInLocators.user_name)
        driver.get_screenshot_as_file("../screenshot/test_positive.png")
        return username.text

    @staticmethod
    def check_error_message():
        driver = LoginPage.login(LogInLocators.username, LogInLocators.invalid_password)
        time.sleep(1)
        error_message = driver.find_element(By.CLASS_NAME, 'el-notification__content')
        driver.get_screenshot_as_file("../screenshot/test_negative.png")
        return error_message.text

