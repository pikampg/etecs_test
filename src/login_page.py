from selenium.webdriver.common.by import By
from config import config


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = config['URL']

    def open(self):
        self.driver.get(self.url)

    def get_username_field(self):
        return self.driver.find_element(By.ID, 'user-name')

    def get_password_field(self):
        return self.driver.find_element(By.ID, 'password')

    def get_login_button(self):
        return self.driver.find_element(By.ID, 'login-button')

    def get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')