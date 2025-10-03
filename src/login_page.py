from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import config


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = config['URL']
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.url)

    def get_username_field(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Логин']"))
        )

    def get_password_field(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Пароль']"))
        )

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[2]/form/button')

    def get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')