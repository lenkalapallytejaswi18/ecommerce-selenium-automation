from data.test_data import SEARCH_PRODUCT
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_product_in_cart(driver):

    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    home_page.search_product(SEARCH_PRODUCT)

    product_page.open_first_product()

    product_page.add_to_cart()

    cart_page.open_cart()

    assert cart_page.product_is_present()


def test_remove_product_from_cart(driver):

    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    home_page.search_product("computer")

    product_page.open_first_product()

    product_page.add_to_cart()

    cart_page.open_cart()

    cart_page.remove_product()

    message = cart_page.get_cart_message()

    assert "Your Shopping Cart is empty!" in message