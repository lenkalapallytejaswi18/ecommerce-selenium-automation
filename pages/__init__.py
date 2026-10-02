def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 15)
    self.logger = get_logger("HomePage")