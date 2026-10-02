from utils.logger import get_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.logger = get_logger("HomePage")

    search_box = (
        By.CSS_SELECTOR,
        "input.search-box-text"
    )

    search_button = (
        By.CSS_SELECTOR,
        "input.search-box-button"
    )

    def search_product(self, product):

        

        search = self.wait.until(
            EC.visibility_of_element_located(self.search_box)
        )

        search.clear()
        search.send_keys(product)

        self.wait.until(
            EC.element_to_be_clickable(self.search_button)
        ).click()
        self.logger.info(f"Searching for product: {product}")