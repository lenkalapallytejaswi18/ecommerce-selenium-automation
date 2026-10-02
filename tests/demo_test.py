from selenium import webdriver


def test_open_website():
    driver = webdriver.Chrome()

    driver.get("https://demowebshop.tricentis.com/")

    assert "Demo Web Shop" in driver.title

    driver.quit()