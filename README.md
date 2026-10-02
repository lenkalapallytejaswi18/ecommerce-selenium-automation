# E-Commerce Web Automation Framework

A Selenium-based test automation framework built using **Python, Selenium WebDriver, and Pytest** to automate functional testing of an e-commerce web application.

## Project Overview

This project automates key user workflows of the **Demo Web Shop** application.

Automated scenarios include:

- Website launch verification
- Product search
- Invalid login validation
- Add product to cart
- Verify product in cart
- Remove product from cart

The framework also includes reusable Page Objects, explicit waits, centralized test data, logging, failure screenshots, and HTML test reporting.

## Application Under Test

**Demo Web Shop**

https://demowebshop.tricentis.com/

## Tech Stack

- **Language:** Python
- **Automation:** Selenium WebDriver
- **Testing Framework:** Pytest
- **Reporting:** Pytest HTML
- **Browser:** Google Chrome
- **Design Pattern:** Page Object Model (POM)
- **Version Control:** Git & GitHub
- **IDE:** Visual Studio Code

## Project Structure

```text
ecommerce-selenium-automation/
│
├── config/
│   └── config.ini
│
├── data/
│   └── test_data.py
│
├── pages/
│   ├── __init__.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── product_page.py
│   └── cart_page.py
│
├── tests/
│   ├── __init__.py
│   ├── demo_test.py
│   ├── login_test.py
│   ├── test_search.py
│   ├── test_product.py
│   └── test_cart.py
│
├── utils/
│   ├── __init__.py
│   ├── config_reader.py
│   └── logger.py
│
├── screenshots/
├── reports/
├── logs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Framework Design

The framework follows the **Page Object Model (POM)** design pattern.

Page-specific classes contain:

- Web element locators
- Page actions
- Explicit waits
- Logging

Test files contain the test scenarios and assertions.

This separation makes the automation code more reusable and maintainable.

## Automated Test Cases

| Test Case | Description |
|---|---|
| `test_open_website` | Verifies that the application opens successfully |
| `test_invalid_login` | Validates login error handling with invalid credentials |
| `test_search_product` | Verifies product search functionality |
| `test_add_product_to_cart` | Verifies that a product can be added to the cart |
| `test_product_in_cart` | Verifies that the selected product appears in the cart |
| `test_remove_product_from_cart` | Verifies product removal from the cart |

## Test Execution

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest -v
```

Generate an HTML test report:

```bash
pytest -v --html=reports/report.html --self-contained-html
```

## Test Results

The current automation suite contains **6 test cases**.

Latest execution:

```text
6 passed
```

## Reporting

The framework generates an HTML report containing:

- Test execution status
- Passed/failed test cases
- Execution duration
- Environment information

Report location:

```text
reports/report.html
```

## Logging

Execution logs are generated in:

```text
logs/test_execution.log
```

The framework records important automation activities such as:

- Opening pages
- Searching for products
- Login actions
- Adding products to cart
- Removing products from cart

## Failure Screenshots

The framework automatically captures a screenshot when a test fails.

Screenshots are stored in:

```text
screenshots/
```

These generated files are excluded from Git using `.gitignore`.

## Configuration

Application configuration is maintained separately in:

```text
config/config.ini
```

Example:

```ini
[DEFAULT]
base_url = https://demowebshop.tricentis.com/
browser = chrome
timeout = 15
```

## Key Automation Concepts Demonstrated

- Selenium WebDriver
- Python automation
- Pytest
- Page Object Model
- Explicit waits
- CSS selectors
- Test assertions
- Test data separation
- Configuration management
- Logging
- HTML reporting
- Failure screenshot capture
- Git & GitHub

## Author

**Tejaswi Lenkalapally**

B.Tech — Computer Science and Engineering (AI & ML)

Aspiring Software Tester / QA Engineer