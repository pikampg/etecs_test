from src.login_page import LoginPage
from config import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open(browser):
    browser.get(config['URL'])

    assert 'Makves' in browser.title


def test_successful_login(browser):
    '''Тест успешного входа в систему'''
    login_page = LoginPage(browser)
    login_page.open()

    login_page.get_username_field().send_keys(config['LOGIN'])
    login_page.get_password_field().send_keys(config['PASSWORD'])
    login_page.get_login_button().click()

    WebDriverWait(browser, 10).until(
        EC.url_changes(browser.current_url)  # Ждем изменения URL
    )
    assert 'dashboard' in browser.current_url
#
#
# def test_logout(logged_in_browser):
#     browser = logged_in_browser
#     browser.find_element(By.ID, 'react-burger-menu-btn').click()
#
#     WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, 'logout_sidebar_link'))
#     ).click()
#
#     login_btn = WebDriverWait(browser, 5).until(
#         EC.presence_of_element_located((By.ID, 'login-button'))
#     )
#     assert login_btn.is_displayed()
