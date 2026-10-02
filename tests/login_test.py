from data.test_data import INVALID_EMAIL, INVALID_PASSWORD
from pages.login_page import LoginPage


def test_invalid_login(driver):

    login_page = LoginPage(driver)

    login_page.open_login_page()

    login_page.enter_email(INVALID_EMAIL)
    login_page.enter_password(INVALID_PASSWORD)

    login_page.click_login()

    error = login_page.get_error_message()

    assert error != ""