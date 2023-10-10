from selenium.webdriver.common.by import By


class LogInLocators:
    assert_value = "Zohrab Harutyunyan"
    username = ("harutyunyan.zohrab.1985@gmail.com")
    expected_error_message = "Invalid login credentials"
    password = "a1234567890"
    invalid_password = "a123456789"
    login_input = (By.ID, "logininput")
    login_button = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div[1]/div/form/div[1]/div[3]/button[1]')
    user_name = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/span/span/button/span[1]')
