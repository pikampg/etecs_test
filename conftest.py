import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import config
from src.login_page import LoginPage


@pytest.fixture(scope='function')
def browser():
    '''Фикстура для запуска браузера Chrome перед тестом и закрытия после'''
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')

    # Создаем драйвер
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def logged_in_browser(browser):
    '''Фикстура для запуска браузера с залогиненным пользователем'''
    login_page = LoginPage(browser)
    login_page.open()

    login_page.get_username_field().send_keys(config['LOGIN'])
    login_page.get_password_field().send_keys(config['PASSWORD'])
    login_page.get_login_button().click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'react-burger-menu-btn'))
    )
    return browser
