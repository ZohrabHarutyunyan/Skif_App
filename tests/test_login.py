from pages.Login_Page import LoginPage
from locators.locators import LogInLocators


def test_login_positive():
    username = LoginPage.check_username()
    assert username == LogInLocators.assert_value


def test_login_negative():
    error_message = LoginPage.check_error_message()
    assert error_message == LogInLocators.expected_error_message





