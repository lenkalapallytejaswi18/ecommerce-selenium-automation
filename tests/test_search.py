from data.test_data import SEARCH_PRODUCT
from pages.home_page import HomePage


def test_search_product(driver):

    home_page = HomePage(driver)

    home_page.search_product(SEARCH_PRODUCT)

    assert "computer" in driver.page_source.lower()
