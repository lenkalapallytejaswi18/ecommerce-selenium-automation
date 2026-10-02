from utils.logger import get_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(driver, 15)
      self.logger = get_logger("CartPage")

    cart_link = (
        By.CSS_SELECTOR,
        "span.cart-label"
    )

    notification = (
        By.CSS_SELECTOR,
        "div.bar-notification.success"
    )

    remove_checkbox = (
        By.CSS_SELECTOR,
        "input[name='removefromcart']"
    )

    update_cart_button = (
        By.CSS_SELECTOR,
        "input[name='updatecart']"
    )

    empty_cart_message = (
        By.CSS_SELECTOR,
        "div.order-summary-content"
    )

    def open_cart(self):
        self.logger.info("Opening shopping cart")

        try:
            self.wait.until(
                EC.invisibility_of_element_located(
                    self.notification
                )
            )
        except:
            pass

        cart = self.wait.until(
            EC.element_to_be_clickable(
                self.cart_link
            )
        )

        cart.click()
        self.logger.info("Shopping cart opened successfully")

    def product_is_present(self):

        products = self.driver.find_elements(
            By.CSS_SELECTOR,
            "input[name='removefromcart']"
        )

        return len(products) > 0

    def remove_product(self):
        self.logger.info("Removing product from cart")

        checkbox = self.wait.until(
            EC.element_to_be_clickable(
                self.remove_checkbox
            )
        )

        checkbox.click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.update_cart_button
            )
        ).click()
        self.logger.info("Product removed from cart")

    def get_cart_message(self):

        message = self.wait.until(
            EC.visibility_of_element_located(
                self.empty_cart_message
            )
        )

        return message.text