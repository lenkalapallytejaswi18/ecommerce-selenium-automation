from data.test_data import SEARCH_PRODUCT
from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_add_product_to_cart(driver):

    home_page = HomePage(driver)
    product_page = ProductPage(driver)

    home_page.search_product(SEARCH_PRODUCT)

    product_page.open_first_product()

    product_page.add_to_cart()

    assert product_page.verify_success_message()