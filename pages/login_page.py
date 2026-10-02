from utils.logger import get_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(driver, 15)
      self.logger = get_logger("LoginPage")

    login_link = (
        By.CSS_SELECTOR,
        "a.ico-login"
    )

    email = (
        By.ID,
        "Email"
    )

    password = (
        By.ID,
        "Password"
    )

    login_button = (
        By.CSS_SELECTOR,
        "input.login-button"
    )

    error_message = (
        By.CSS_SELECTOR,
        "div.validation-summary-errors"
    )

    def open_login_page(self):
        self.logger.info("Opening login page")

        self.wait.until(
            EC.element_to_be_clickable(
                self.login_link
            )
        ).click()
        self.logger.info("Login page opened successfully")

    def enter_email(self, email):

        self.wait.until(
            EC.visibility_of_element_located(
                self.email
            )
        ).send_keys(email)

    def enter_password(self, password):
        self.logger.info("Entering email")

        self.wait.until(
            EC.visibility_of_element_located(
                self.password
            )
        ).send_keys(password)

    def click_login(self):
        self.logger.info("Clicking login button")

        self.wait.until(
            EC.element_to_be_clickable(
                self.login_button
            )
        ).click()

    def get_error_message(self):

        error = self.wait.until(
            EC.visibility_of_element_located(
                self.error_message
            )
        )
        self.logger.info("Login error message captured")
        return error.text