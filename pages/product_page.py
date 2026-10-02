from utils.logger import get_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver):
       
      self.driver = driver
      self.wait = WebDriverWait(driver, 15)
      self.logger = get_logger("ProductPage")

    product_link = (
        By.CSS_SELECTOR,
        "h2.product-title a"
    )

    add_to_cart_button = (
        By.CSS_SELECTOR,
        "input[value='Add to cart']"
    )

    success_message = (
        By.CSS_SELECTOR,
        "div.bar-notification.success"
    )

    cart_quantity = (
        By.CSS_SELECTOR,
        "span.cart-qty"
    )

    def open_first_product(self):
       self.logger.info("Opening first product")
       

       for attempt in range(3):

        try:
            product = self.driver.find_element(
                *self.product_link
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                product
            )

            product.click()
            self.logger.info("First product opened successfully")
            return

        except Exception:
            if attempt == 2:
                raise

            self.driver.refresh()

            self.wait.until(
                EC.presence_of_element_located(
                    self.product_link
                )
            )

    def add_to_cart(self):


        self.logger.info("Adding product to cart")

        button = self.wait.until(
        EC.element_to_be_clickable(self.add_to_cart_button)
    )

        button.click()

        self.wait.until(
        EC.visibility_of_element_located(self.success_message)
    )

        self.wait.until(
        lambda driver:
        driver.find_element(
            *self.cart_quantity
        ).text.strip() != "(0)"
    )

        self.logger.info("Product added to cart successfully")
    def verify_success_message(self):

      message = self.wait.until(
        EC.visibility_of_element_located(
            self.success_message
        )
    )

      self.logger.info("Success message verified")

      return message.is_displayed()